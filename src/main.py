from PyQt6.QtWidgets import QApplication
from threading import Thread
import sys

from application import app
from routes.akunRoutes import akunRoutes
from routes.permintaanRoutes import permintaanRoutes
from routes.transaksiRoutes import transaksiRoutes
from routes.lamanRoutes import lamanRoutes
from views import pageController

def loadBackend():
    app.register_blueprint(akunRoutes, url_prefix="/akun")
    app.register_blueprint(permintaanRoutes, url_prefix="/permintaan")
    app.register_blueprint(transaksiRoutes, url_prefix="/transaksi")
    app.register_blueprint(lamanRoutes, url_prefix="/laman")

    app.run(port=3000, debug=True, use_reloader=False)

if __name__ == "__main__":
    threadBackend = Thread(target=loadBackend)
    threadBackend.setDaemon(True)
    threadBackend.start()

    window = QApplication(sys.argv)
    view = pageController.PageController() # JANGAN HAPUS VARIABLE VIEWNYA YA BEBZ
    sys.exit(window.exec())