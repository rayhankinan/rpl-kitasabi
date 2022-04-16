from flask import Blueprint

from controllers.transaksiControllers import TransaksiController

transaksiRoutes = Blueprint("transaksiRoutes", __name__)

transaksiRoutes.route("/bayar", methods=["POST"]) (TransaksiController.bayar)
transaksiRoutes.route("/riwayat_donatur", methods=["GET"]) (TransaksiController.riwayatDonatur)
transaksiRoutes.route("/riwayat_penggalang", methods=["GET"]) (TransaksiController.riwayatPenggalang)
transaksiRoutes.route("/cair", methods=["PUT"]) (TransaksiController.cair)