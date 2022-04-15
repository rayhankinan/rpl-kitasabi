from email_validator import validate_email, EmailNotValidError
import phonenumbers
import bcrypt

from models.db import mysql
from models.cdn import bucket

class Akun:
    # CONSTRUCTOR
    def __init__(self, email, listNoTelp, namaDepan, namaBelakang, username, password, foto):
        # VALIDATE EMAIL
        try:
            valid = validate_email(email)
            self.email = valid.ascii_email

        except EmailNotValidError:
            raise Exception(f"{email} bukanlah email yang valid!")

        # VALIDATE PHONE NUMBER
        self.listNoTelp = []
        for noTelp in listNoTelp:
            if not phonenumbers.is_possible_number(phonenumbers.parse(noTelp)):
                raise Exception(f"{noTelp} bukanlah nomor telepon yang valid!")
            elif not phonenumbers.is_valid_number(phonenumbers.parse(noTelp)):
                raise Exception(f"{noTelp} tidak terdaftar pada provider apapun!")
            elif noTelp in self.listNoTelp:
                raise Exception(f"{noTelp} sudah terdaftar pada sistem!")
            else:
                # UPDATE ATTRIBUTE
                self.listNoTelp.append(noTelp)

        # VALIDATE NAMA
        if not namaDepan.isalpha():
            raise Exception(f"{namaDepan} bukanlah nama yang valid!")
        else:
            self.namaDepan = namaDepan

        if not namaBelakang.isalpha():
            raise Exception(f"{namaBelakang} bukanlah nama yang valid!")
        else:
            self.namaBelakang = namaBelakang

        if not username.isalnum():
            raise Exception(f"{username} bukanlah username yang valid!")
        else:
            self.username = username

        if len(password) < 8:
            raise Exception(f"Password {password} memiliki panjang kurang dari 8!")
        else:
            self.hashedPassword = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())

        # UPLOAD FOTO JIKA ADA
        if foto is not None:
            blob = bucket.blob(foto.filename)
            blob.upload_from_string(foto.stream.read())

            self.gcloudURL = blob.public_url
        else:
            self.gcloudURL = None

        # INISIALISASI CURSOR
        cursor = mysql.connection.cursor()

        # MASUKKAN AKUN KE DALAM DATABASE
        cursor.execute("INSERT INTO Akun (Email, NamaDepan, NamaBelakang, Username, Password, Foto) VALUES (%s, %s, %s, %s, %s, %s)", (self.email, self.namaDepan, self.namaBelakang, self.username, self.hashedPassword, self.gcloudURL))

        # MASUKKAN NO TELP KE DALAM DATABASE
        for noTelp in self.listNoTelp:
            cursor.execute("INSERT INTO Akun_No_Telp (IDPengguna, NoTelp) SELECT MAX(IDPengguna), %s FROM Akun", (noTelp, ))
        
        # TUTUP CURSOR
        mysql.connection.commit()
        cursor.close()

    # CLASS METHOD
    @classmethod
    def getByEmailOrUsername(cls, emailOrUsername):
        cursor = mysql.connection.cursor()

        cursor.execute("SELECT Email, NamaDepan, NamaBelakang, Username, Password, Foto FROM Akun WHERE Email = %s OR Username = %s", (emailOrUsername, emailOrUsername))
        dataAkun = cursor.fetchone()

        cursor.execute("SELECT NoTelp FROM Akun_No_Telp NATURAL JOIN Akun WHERE Email = %s OR Username = %s", (emailOrUsername, emailOrUsername))
        dataNoTelp = cursor.fetchall()

        cursor.close()

        if dataAkun is None:
            raise Exception(f"Username atau Email {emailOrUsername} belum terdaftar pada sistem!")
        else:
            email, namaDepan, namaBelakang, username, hashedPassword, gcloudURL = dataAkun
            listNoTelp = dataNoTelp

            self = cls.__new__(cls)
            self.email = email
            self.listNoTelp = listNoTelp
            self.namaDepan = namaDepan
            self.namaBelakang = namaBelakang
            self.username = username
            self.hashedPassword = hashedPassword
            self.gcloudURL = gcloudURL
            
            return self

    # ATTRIBUTE METHOD
    def getEmail(self):
        return self.email

    def getListNoTelp(self):
        return self.listNoTelp

    def addNoTelp(self, noTelp):
        if not phonenumbers.is_possible_number(phonenumbers.parse(noTelp)):
            raise Exception(f"{noTelp} bukanlah nomor telepon yang valid!")
        elif not phonenumbers.is_valid_number(phonenumbers.parse(noTelp)):
            raise Exception(f"{noTelp} tidak terdaftar pada provider apapun!")
        elif noTelp in self.listNoTelp:
            raise Exception(f"{noTelp} sudah terdaftar pada sistem!")
        else:
            # UPDATE ATTRIBUTE
            self.listNoTelp.append(noTelp)

            # INISIALISASI CURSOR
            cursor = mysql.connection.cursor()

            cursor.execute("INSERT INTO Akun_No_Telp (IDPengguna, NoTelp) SELECT MAX(IDPengguna), %s FROM Akun", (noTelp, ))

            # TUTUP CURSOR
            mysql.connection.commit()
            cursor.close()

    def deleteNoTelp(self, noTelp):
        # UPDATE ATTRIBUTE
        self.listNoTelp.remove(noTelp)

        # INISIALISASI CURSOR
        cursor = mysql.connection.cursor()

        cursor.execute("DELETE FROM Akun_No_Telp WHERE IDPengguna = (SELECT IDPengguna FROM Akun WHERE Email = %s) AND NoTelp = %s", (self.email, noTelp))

        # TUTUP CURSOR
        mysql.connection.commit()
        cursor.close()

    def getNamaDepan(self):
        return self.namaDepan

    def getNamaBelakang(self):
        return self.namaBelakang

    def getNamaLengkap(self):
        return f"{self.namaDepan} {self.namaBelakang}"

    def getUsername(self):
        return self.username

    def setUsername(self, username):
        if not username.isalnum():
            raise Exception(f"{username} bukanlah username yang valid!")
        else:
            # UPDATE ATTRIBUTE
            self.username = username

            # INISIALISASI CURSOR
            cursor = mysql.connection.cursor()

            cursor.execute("UPDATE Akun SET Username = %s WHERE Email = %s", (self.username, self.email))

            # TUTUP CURSOR
            mysql.connection.commit()
            cursor.close()

    def matchPassword(self, password):
        return bcrypt.checkpw(password.encode("utf-8"), self.hashedPassword)

    def getHashedPassword(self):
        return self.hashedPassword

    def setPassword(self, password):
        if len(password) < 8:
            raise Exception(f"Password {password} memiliki panjang kurang dari 8!")
        else:
            # UPDATE ATTRIBUTE
            self.hashedPassword = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())

            # INISIALISASI CURSOR
            cursor = mysql.connection.cursor()

            cursor.execute("UPDATE Akun SET Password = %s WHERE Email = %s", (self.hashedPassword, self.email))

            # TUTUP CURSOR
            mysql.connection.commit()
            cursor.close()

    def getGcloudURL(self):
        return self.gcloudURL

    def setFoto(self, foto):
        # DELETE FOTO
        blob = bucket.blob(self.gcloudURL.rsplit("/", 1)[-1])
        blob.delete()

        # UPLOAD FOTO
        blob = bucket.blob(foto.filename)
        blob.upload_from_string(foto.stream.read())

        # UPDATE ATTRIBUTE
        self.gcloudURL = blob.public_url

        # INISIALISASI CURSOR
        cursor = mysql.connection.cursor()

        cursor.execute("UPDATE Akun SET Foto = %s WHERE Email = %s", (self.gcloudURL, self.email))

        # TUTUP CURSOR
        mysql.connection.commit()
        cursor.close()

    def deleteFoto(self):
        # DELETE FOTO
        blob = bucket.blob(self.gcloudURL.rsplit("/", 1)[-1])
        blob.delete()

        # UPDATE ATTRIBUTE
        self.gcloudURL = None

        # INISIALISASI CURSOR
        cursor = mysql.connection.cursor()

        cursor.execute("UPDATE Akun SET Foto = NULL WHERE Email = %s", (self.email, ))

        # TUTUP CURSOR
        mysql.connection.commit()
        cursor.close()

    # PROCEDURAL METHOD
    def delete(self):
        # HAPUS DARI CDN
        self.deleteFoto()

        # INISIALISASI CURSOR
        cursor = mysql.connection.cursor()

        cursor.execute("DELETE FROM Akun WHERE Email = %s", (self.email, ))

        # TUTUP CURSOR
        mysql.connection.commit()
        cursor.close()