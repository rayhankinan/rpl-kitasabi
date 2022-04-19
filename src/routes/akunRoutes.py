from flask import Blueprint

from controllers.akunControllers import AkunController

akunRoutes = Blueprint("akunRoutes", __name__)

akunRoutes.route("/register", methods=["POST"]) (AkunController.register)
akunRoutes.route("/login", methods=["GET"]) (AkunController.login)
akunRoutes.route("/profile", methods=["GET"]) (AkunController.profile)
akunRoutes.route("/edit", methods=["PUT"]) (AkunController.edit)
akunRoutes.route("/delete", methods=["DELETE"]) (AkunController.delete)