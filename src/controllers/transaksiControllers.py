from flask import request, session, jsonify
import json

class TransaksiController:
    @staticmethod
    def bayar():
        try:
            data = json.loads(session["User"])
            

            return "Created", 201
        except Exception as e:
            return str(e), 400

    @staticmethod
    def riwayatDonatur():
        return "OK", 200

    @staticmethod
    def cair():
        return "OK", 200

    @staticmethod
    def riwayatPenggalang():
        return "OK", 200