from flask import Blueprint

from controllers.akunControllers import AkunController

akunRoutes = Blueprint("akunRoutes", __name__)

akunRoutes.route("/login", methods=["POST"]) (AkunController.login)
akunRoutes.route("/logout", methods=["POST"]) (AkunController.logout)
akunRoutes.route("/register", methods=["POST"]) (AkunController.register)
akunRoutes.route("/edit", methods=["PUT"]) (AkunController.edit)
akunRoutes.route("/delete", methods=["DELETE"]) (AkunController.delete)