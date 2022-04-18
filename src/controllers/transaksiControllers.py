from flask import request, session, jsonify
from datetime import datetime
import json

from models.lamanModels import Laman
from models.transaksiModels import Transaksi

class TransaksiController:
    @staticmethod
    def bayar():
        try:
            data = json.loads(session["User"])

            idDonatur = data["ID"]
            idLaman = int(request.form.get("id-laman"))
            jumlahTransaksi = int(request.form.get("jumlah-transaksi"))

            if Laman.getByIDLaman(idLaman).getDeadline() > datetime.date(datetime.now()):
                return "Conflict", 409 

            else:
                Transaksi(idDonatur, idLaman, jumlahTransaksi)

            return "Created", 201

        except Exception as e:
            return str(e), 400

    @staticmethod
    def riwayatDonatur():
        try:
            data = json.loads(session["User"])
            idDonatur = data["ID"]

            result = []
            riwayatTransaksi = Transaksi.getRiwayatDonasi(idDonatur)
            for transaksi in riwayatTransaksi:
                result.append({
                    "idTransaksi": transaksi.getIDTransaksi(), 
                    "idDonatur": transaksi.getIDDonatur(), 
                    "idLaman": transaksi.getIDLaman(), 
                    "jumlahTransaksi": transaksi.getJumlahTransaksi(), 
                    "timestamp": transaksi.getTimestamp(), 
                    "statusPencairan": transaksi.getStatusPencairan()
                })

            return jsonify(result), 200

        except Exception as e:
            return str(e), 400

    @staticmethod
    def cair():
        try:
            idLaman = int(request.form.get("id-laman"))

            if Laman.getByIDLaman(idLaman).getDeadline() < datetime.date(datetime.now()):
                return "Conflict", 409
            
            else:
                riwayatTransaksi = Transaksi.getRiwayatLaman(idLaman)
                for transaksi in riwayatTransaksi:
                    transaksi.cairkanTransaksi()

                return "OK", 200

        except Exception as e:
            return str(e), 400

    @staticmethod
    def riwayatLaman():
        try:
            idLaman = int(request.form.get("id-laman"))

            result = []
            riwayatTransaksi = Transaksi.getRiwayatLaman(idLaman)
            for transaksi in riwayatTransaksi:
                result.append({
                    "idTransaksi": transaksi.getIDTransaksi(), 
                    "idDonatur": transaksi.getIDDonatur(), 
                    "idLaman": transaksi.getIDLaman(), 
                    "jumlahTransaksi": transaksi.getJumlahTransaksi(), 
                    "timestamp": transaksi.getTimestamp(), 
                    "statusPencairan": transaksi.getStatusPencairan()
                })

            return jsonify(result), 200
            
        except Exception as e:
            return str(e), 400