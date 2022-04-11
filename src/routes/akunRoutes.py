from flask import Blueprint

from application import app
from controllers.akunControllers import login, register, logout, edit, delete

akunRoutes = Blueprint("akunRoutes", __name__)

akunRoutes.route("/login", methods=["POST"]) (login)
akunRoutes.route("/logout", methods=["POST"]) (register)
akunRoutes.route("/register", methods=["POST"]) (logout)
akunRoutes.route("/edit", methods=["PUT"]) (edit)
akunRoutes.route("/delete", methods=["DELETE"]) (delete)

app.register_blueprint(akunRoutes, url_prefix="/akun")