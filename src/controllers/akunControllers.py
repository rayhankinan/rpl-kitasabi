from flask import request, jsonify

from models.akunModels import Akun
from application import auth

class AkunController:
    @staticmethod
    @auth.verify_password
    def authenticate(emailOrUsername, password):
        try:
            akun = Akun.getByEmailOrUsername(emailOrUsername)

            if akun.matchPassword(password):
                return akun
            else:
                return None

        except:
            return None

    @staticmethod
    def register():
        try:
            email = request.form.get("email")
            listNoTelp = list(request.form.getlist("no-telp"))
            namaDepan = request.form.get("nama-depan")
            namaBelakang = request.form.get("nama-belakang")
            username = request.form.get("username")
            password = request.form.get("password")
            foto = request.files.get("foto")

            Akun(email, listNoTelp, namaDepan, namaBelakang, username, password, foto)

            return "Created", 201

        except Exception as e:
            return str(e), 400

    @staticmethod
    @auth.login_required
    def profile():
        try:
            akun = auth.current_user()

            return jsonify(email=akun.getEmail(), listNoTelp=akun.getListNoTelp(), namaDepan=akun.getNamaDepan(), namaBelakang=akun.getNamaBelakang(), username=akun.getUsername(), foto=akun.getGcloudURL()), 200

        except Exception as e:
            return str(e), 400

    @staticmethod
    @auth.login_required
    def edit():
        try:
            username = request.form.get("username")
            password = request.form.get("password")
            foto = request.files.get("foto")

            akun = auth.current_user()

            akun.setUsername(username)
            akun.setPassword(password)
            akun.setFoto(foto)

            return "OK", 200

        except Exception as e:
            return str(e), 400

    @staticmethod
    @auth.login_required
    def delete():
        try:
            akun = auth.current_user()
            akun.delete()

            return "OK", 200

        except Exception as e:
            return str(e), 400