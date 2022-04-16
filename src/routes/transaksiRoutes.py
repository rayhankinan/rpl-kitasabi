from flask import Blueprint

from controllers.transaksiControllers import TransaksiController

transaksiRoutes = Blueprint("transaksiRoutes", __name__)

transaksiRoutes.route("/bayar", methods=["POST"]) (TransaksiController.bayar)
transaksiRoutes.route("/riwayat-donatur", methods=["GET"]) (TransaksiController.riwayatDonatur)
transaksiRoutes.route("/riwayat-laman", methods=["GET"]) (TransaksiController.riwayatLaman)
transaksiRoutes.route("/cair", methods=["PUT"]) (TransaksiController.cair)