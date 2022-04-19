from flask import request, jsonify
from datetime import datetime

from models.lamanModels import Laman
from models.transaksiModels import Transaksi
from application import userAuth

class TransaksiController:
    @staticmethod
    @userAuth.login_required
    def bayar():
        try:
            data = userAuth.current_user()

            idDonatur = data.getIDPengguna()
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
    @userAuth.login_required
    def riwayatDonatur():
        try:
            data = userAuth.current_user()
            idDonatur = data.getIDPengguna()

            result = []
            riwayatTransaksi = Transaksi.getRiwayatDonasi(idDonatur)
            for transaksi in riwayatTransaksi:
                result.append({
                    "id-transaksi": transaksi.getIDTransaksi(), 
                    "id-donatur": transaksi.getIDDonatur(), 
                    "id-daman": transaksi.getIDLaman(), 
                    "jumlah-transaksi": transaksi.getJumlahTransaksi(), 
                    "timestamp": transaksi.getTimestamp(), 
                    "status-pencairan": transaksi.getStatusPencairan()
                })

            return jsonify(result), 200

        except Exception as e:
            return str(e), 400

    @staticmethod
    @userAuth.login_required
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
    @userAuth.login_required
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