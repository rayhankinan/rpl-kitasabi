from email_validator import validate_email, EmailNotValidError
from phonenumbers import is_possible_number, is_valid_number
import bcrypt

from db import mysql
from cdn import imageBucket

class Akun:
    def __init__(self, email, noTelp, namaDepan, namaBelakang, username, password, foto):
        self.email = email
        self.noTelp = noTelp
        self.namaDepan = namaDepan
        self.namaBelakang = namaBelakang
        self.username = username
        self.password = password
        self.foto = foto

    def create(self):
        try:
            valid = validate_email(self.email)
            self.email = valid.email

        except EmailNotValidError:
            raise Exception(f"{self.email} bukanlah email yang valid!")

        if not is_possible_number(self.noTelp):
            raise Exception(f"{self.noTelp} bukanlah nomor telepon yang valid!")

        if not is_valid_number(self.noTelp):
            raise Exception(f"{self.noTelp} tidak terdaftar pada provider apapun!")

        if not self.namaDepan.isalpha():
            raise Exception(f"{self.namaDepan} bukanlah nama yang valid!")

        if not self.namaBelakang.isalpha():
            raise Exception(f"{self.namaBelakang} bukanlah nama yang valid!")

        # VALIDATE USERNAME

        # VALIDATE PASSWORD

        # VALIDATE FOTO