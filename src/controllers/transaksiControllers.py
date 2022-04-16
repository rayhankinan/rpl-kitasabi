from flask import request, session, jsonify
import json

from models.transaksiModels import Transaksi

class TransaksiController:
    @staticmethod
    def bayar():
        try:
            data = json.loads(session["User"])

            idDonatur = data["ID"]
            idLaman = int(request.form.get("id-laman"))
            jumlahTransaksi = int(request.form.get("jumlah-transaksi"))
            
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
                result.append({"idTransaksi": transaksi.getIDTransaksi(), "idDonatur": transaksi.getIDDonatur(), "idLaman": transaksi.getIDLaman(), "jumlahTransaksi": transaksi.getJumlahTransaksi(), "timestamp": transaksi.getTimestamp(), "statusPencairan": transaksi.getStatusPencairan()})

            return jsonify(result), 200

        except Exception as e:
            return str(e), 400

    @staticmethod
    def cair():
        try:
            data = json.loads(session["User"])
            idDonatur = data["ID"]
            idLaman = int(request.form.get("id-laman"))
            timestamp = request.form.get("timestamp")

            Transaksi.getByDonaturLamanTimestamp(idDonatur, idLaman, timestamp).cairkanTransaksi()

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
                result.append({"idTransaksi": transaksi.getIDTransaksi(), "idDonatur": transaksi.getIDDonatur(), "idLaman": transaksi.getIDLaman(), "jumlahTransaksi": transaksi.getJumlahTransaksi(), "timestamp": transaksi.getTimestamp(), "statusPencairan": transaksi.getStatusPencairan()})

            return jsonify(result), 200
            
        except Exception as e:
            return str(e), 400