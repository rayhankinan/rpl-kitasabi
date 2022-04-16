from flask import Blueprint
from controllers.permintaanControllers import PermintaanController

permintaanRoutes = Blueprint("permintaanRoutes", __name__)

permintaanRoutes.route("/create-permintan-kesehatan", methods=["POST"]) (PermintaanController.createPermintaanKesehatan)
permintaanRoutes.route("/create-permintan-lainnya", methods=["POST"]) (PermintaanController.createPermintaanLainnya)
permintaanRoutes.route("/setujui-permintaan-kesehatan", methods=["PUT"]) (PermintaanController.setujuiPermintaanKesehatan)
permintaanRoutes.route("/setujui-permintaan-lainnya", methods=["PUT"]) (PermintaanController.setujuiPermintaanLainnya)
permintaanRoutes.route("/riwayat-permintaan", methods=["GET"]) (PermintaanController.riwayatPermintaan)
