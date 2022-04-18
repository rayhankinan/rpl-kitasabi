from application import app
from views import pageController
from routes.akunRoutes import akunRoutes
from routes.permintaanRoutes import permintaanRoutes
from routes.transaksiRoutes import transaksiRoutes
from routes.lamanRoutes import lamanRoutes
from PyQt6.QtWidgets import QApplication
import sys
import threading

if __name__ == "__main__":
    app.register_blueprint(akunRoutes, url_prefix="/akun")
    app.register_blueprint(permintaanRoutes, url_prefix="/permintaan")
    app.register_blueprint(transaksiRoutes, url_prefix="/transaksi")
    app.register_blueprint(lamanRoutes, url_prefix="/laman")

    app.run(port=3000, debug=True)

    # window = QApplication(sys.argv)
    # view = pageController.PageController()
    # sys.exit(window.exec())