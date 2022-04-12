from application import app
from routes.akunRoutes import akunRoutes

routed_app = app

routed_app.register_blueprint(akunRoutes, url_prefix="/akun")