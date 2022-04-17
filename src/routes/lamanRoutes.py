from flask import Blueprint

from controllers.lamanControllers import LamanController

lamanRoutes = Blueprint("lamanRoutes", __name__)

lamanRoutes.route("eksplor-kategori", methods=["GET"]) (LamanController.eksplorKategoriLaman)
lamanRoutes.route("eksplor-total-donasi", methods=["GET"]) (LamanController.eksplorTotalDonasiLaman)
lamanRoutes.route("detail-laman", methods=["GET"]) (LamanController.detailLaman)
lamanRoutes.route("riwayat-laman", methods=["GET"]) (LamanController.riwayatLaman)
lamanRoutes.route("create-laman", methods=["POST"]) (LamanController.createLaman)
lamanRoutes.route("search-laman", methods=["POST"]) (LamanController.searchlaman)
lamanRoutes.route("edit-laman", methods=["PUT"]) (LamanController.editLaman)

