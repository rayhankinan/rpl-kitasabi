from flask import Blueprint

from controllers.akunControllers import login, register, logout, edit, delete

akunRoutes = Blueprint("akunRoutes", __name__)

akunRoutes.route("/login", methods=["POST"]) (login)
akunRoutes.route("/logout", methods=["POST"]) (logout)
akunRoutes.route("/register", methods=["POST"]) (register)
akunRoutes.route("/edit", methods=["PUT"]) (edit)
akunRoutes.route("/delete", methods=["DELETE"]) (delete)