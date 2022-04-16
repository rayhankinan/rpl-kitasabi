from crypt import methods
from flask import Blueprint
from controllers.permintaanControllers import PermintaanController

permintaanRoutes = Blueprint("permintaanRoutes", __name__)

permintaanRoutes.route("/create-permintan-kesehatan", methods=["POST"]) (PermintaanController.createPermintaanKesehatan)
permintaanRoutes.route("/create-permintan-lainnya", methods=["POST"]) (PermintaanController.createPermintaanLainnya)
permintaanRoutes.route("/edit-permintaan", methods=["PUT"]) (PermintaanController.setujuiPermintaan)
permintaanRoutes.route("/riwayat-permintaan", methods=["GET"]) (PermintaanController.riwayat)
