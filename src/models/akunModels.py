from db import mysql

class Akun:
    def __init__(self, email, noTelp, namaDepan, namaBelakang, username, password, foto):
        self.email = email
        self.noTelp = noTelp
        self.namaDepan = namaDepan
        self.namaBelakang = namaBelakang
        self.username = username
        self.password = password
        self.foto = foto

    def create():
        pass