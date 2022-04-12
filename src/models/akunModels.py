from email_validator import validate_email, EmailNotValidError
import phonenumbers
import bcrypt

from models.db import mysql
from models.cdn import bucket

class Akun:
    # STATIC METHOD
    def getByEmailOrUsername(emailOrUsername):
        cursor = mysql.connection.cursor()

        cursor.execute("SELECT Email, NamaDepan, NamaBelakang, Username, Password, Foto FROM Akun WHERE Email = %s OR Username = %s", (emailOrUsername, emailOrUsername))
        dataAkun = cursor.fetchall()

        cursor.execute("SELECT NoTelp FROM Akun_No_Telp NATURAL JOIN Akun WHERE Email = %s OR Username = %s", (emailOrUsername, emailOrUsername))
        dataNoTelp = cursor.fetchall()

        cursor.close()

        if len(dataAkun) == 0:
            raise Exception(f"Username atau Email {emailOrUsername} belum terdaftar pada sistem!")
        elif len(dataAkun) > 1:
            raise Exception(f"Terdapat kesalahan pada server!")
        else:
            pass # FIX THIS

    # NONSTATIC METHOD
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
            self.addNoTelp(noTelp)

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
            self.setFoto(foto)

    # EMAIL
    def getEmail(self):
        return self.email

    # NO TELP
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
            self.listNoTelp.append(noTelp)

    def deleteNoTelp(self, noTelp):
        self.listNoTelp.remove(noTelp)

    # NAMA
    def getNamaDepan(self):
        return self.namaDepan

    def getNamaBelakang(self):
        return self.namaBelakang

    def getNamaLengkap(self):
        return f"{self.namaDepan} {self.namaBelakang}"

    # USERNAME
    def getUsername(self):
        return self.username

    def setUsername(self, username):
        self.username = username

    # PASSWORD
    def matchPassword(self, password):
        return bcrypt.checkpw(password.encode("utf-8"), self.hashedPassword)

    def getHashedPassword(self):
        return self.hashedPassword

    def setPassword(self, password):
        self.hashedPassword = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())

    # FOTO
    def getGcloudURL(self):
        return self.gcloudURL

    def setFoto(self, foto):
        blob = bucket.blob(foto.filename)
        blob.upload_from_string(foto.stream.read())

        self.gcloudURL = blob.public_url

    # CLASS METHOD
    def create(self):
        # INISIALISASI CURSOR
        cursor = mysql.connection.cursor()

        # MASUKKAN AKUN KE DALAM DATABASE
        cursor.execute("INSERT INTO Akun (Email, NamaDepan, NamaBelakang, Username, Password, Foto) VALUES (%s, %s, %s, %s, %s, %s)", (self.email, self.namaDepan, self.namaBelakang, self.username, self.hashedPassword, self.gcloudURL))
        mysql.connection.commit()

        # MASUKKAN NO TELP KE DALAM DATABASE
        for noTelp in self.listNoTelp:
            cursor.execute("INSERT INTO Akun_No_Telp (IDPengguna, NoTelp) SELECT MAX(IDPengguna), %s FROM Akun", (noTelp, ))
        mysql.connection.commit()

        # TUTUP CURSOR
        cursor.close()

    def update(self):
        pass

    def delete(self):
        pass