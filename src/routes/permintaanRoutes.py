from flask import Blueprint
from controllers.permintaanControllers import PermintaanController

permintaanRoutes = Blueprint("permintaanRoutes", __name__)

permintaanRoutes.route("/create-permintaan-kesehatan", methods=["POST"]) (PermintaanController.createPermintaanKesehatan)
permintaanRoutes.route("/create-permintaan-lainnya", methods=["POST"]) (PermintaanController.createPermintaanLainnya)
permintaanRoutes.route("/riwayat-permintaan", methods=["GET"]) (PermintaanController.riwayatPermintaan)
permintaanRoutes.route("/edit-permintaan-kesehatan", methods=["PUT"]) (PermintaanController.editStatusPermintaanKesehatan)
permintaanRoutes.route("/edit-permintaan-lainnya", methods=["PUT"]) (PermintaanController.editStatusPermintaanLainnya)
permintaanRoutes.route("/detail-permintaan", methods=["GET"]) (PermintaanController.detailPermintaan)