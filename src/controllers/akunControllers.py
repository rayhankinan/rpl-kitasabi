from flask import request, session
import json

from models.akunModels import Akun

class AkunController:
    @staticmethod
    def login():
        try:
            emailOrUsername = request.form.get("email-username")
            password = request.form.get("password")

            newAkun = Akun.getByEmailOrUsername(emailOrUsername)

            if newAkun.matchPassword(password):
                session["User"] = json.dumps({"email": newAkun.getEmail(), "username": newAkun.getUsername()})
                return "Created", 201

            else:
                return "Unauthorized", 401

        except Exception as e:
            return str(e), 400

    @staticmethod
    def register():
        try:
            email = request.form.get("email")
            listNoTelp = request.form.getlist("no-telp")
            namaDepan = request.form.get("nama-depan")
            namaBelakang = request.form.get("nama-belakang")
            username = request.form.get("username")
            password = request.form.get("password")
            foto = request.files.get("foto")

            newAkun = Akun(email, listNoTelp, namaDepan, namaBelakang, username, password, foto)

            return "Created", 201

        except Exception as e:
            return str(e), 400

    @staticmethod
    def logout():
        try:
            session["User"] = None
            return "Created", 201

        except Exception as e:
            return str(e), 400

    @staticmethod
    def edit():
        return "Bad Request", 400

    @staticmethod
    def delete():
        return "Bad Request", 400