from flask import request, session
import json

from models.akunModels import Akun

def login():
    try:
        emailOrUsername = request.form.get("email-username")
        password = request.form.get("password")

        user = Akun.getByEmailOrUsername(emailOrUsername)

        if user.matchPassword(password):
            session["User"] = json.dumps(email=user.getEmail(), username=user.getUsername())
        else:
            return "Unauthorized", 401

    except Exception as e:
        return str(e), 400

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
        newAkun.create()

        return "Created", 201

    except Exception as e:
        return str(e), 400

def logout():
    return "Bad Request", 400

def edit():
    return "Bad Request", 400

def delete():
    return "Bad Request", 400