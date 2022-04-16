from application import app
from routes.akunRoutes import akunRoutes
from routes.permintaanRoutes import permintaanRoutes
from routes.transaksiRoutes import transaksiRoutes

if __name__ == "__main__":
    app.register_blueprint(akunRoutes, url_prefix="/akun")
    app.register_blueprint(permintaanRoutes, url_prefix="/permintaan")
    app.register_blueprint(transaksiRoutes, url_prefix="/transaksi")

    app.run(port=3000, debug=True)