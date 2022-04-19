from flask import Blueprint

from controllers.akunControllers import AkunController

akunRoutes = Blueprint("akunRoutes", __name__)

akunRoutes.route("/register", methods=["POST"]) (AkunController.register)
akunRoutes.route("/login", methods=["GET"]) (AkunController.login)
akunRoutes.route("/profile", methods=["GET"]) (AkunController.profile)
akunRoutes.route("/edit-username-password", methods=["PUT"]) (AkunController.editUsernamePassword)
akunRoutes.route("/edit-foto", methods=["PUT"]) (AkunController.editFoto)
akunRoutes.route("/delete", methods=["DELETE"]) (AkunController.delete)