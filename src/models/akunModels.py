from email_validator import validate_email, EmailNotValidError
from phonenumbers import is_possible_number, is_valid_number, parse
import bcrypt

from models.db import mysql
from models.cdn import bucket

class Akun:
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
            if not is_possible_number(parse(noTelp)):
                raise Exception(f"{noTelp} bukanlah nomor telepon yang valid!")
            elif not is_valid_number(parse(noTelp)):
                raise Exception(f"{noTelp} tidak terdaftar pada provider apapun!")
            else:
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

        # NO VALIDATION REQUIRED
        self.username = username
        self.password = password
        self.foto = foto

    def create(self):
        # HASH PASSWORD
        hashedPassword = bcrypt.hashpw(self.password.encode("utf-8"), bcrypt.gensalt())

        # UPLOAD FOTO
        blob = bucket.blob(self.foto.filename)
        blob.upload_from_string(self.foto.stream.read())

        gcloudURL = f"https://storage.googleapis.com/{bucket.name}/{blob.name}"

        # MASUKKAN AKUN KE DALAM DATABASE
        cursor = mysql.connection.cursor()

        cursor.execute("INSERT INTO Akun (Email, NamaDepan, NamaBelakang, Username, Password, Foto) VALUES (%s, %s, %s, %s, %s, %s)", (self.email, self.namaDepan, self.namaBelakang, self.username, hashedPassword, gcloudURL))
        
        mysql.connection.commit()
        cursor.close()

        # MASUKKAN NO TELP KE DALAM DATABASE
        cursor = mysql.connection.cursor()

        for noTelp in self.listNoTelp:
            cursor.execute("INSERT INTO Akun_No_Telp (IDPengguna, NoTelp) SELECT MAX(IDPengguna), %s FROM Akun", (noTelp, ))

        mysql.connection.commit()
        cursor.close()