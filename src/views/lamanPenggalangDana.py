from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton
from PyQt6.QtGui import QCursor, QIcon
from PyQt6.QtCore import pyqtSignal, Qt
from views.formKesehatan import FormKesehatan
from views.formNonKesehatan import FormNonKesehatan
import sys, pathlib

class LamanPenggalangDana(QWidget): # TODO: BUAT LAMAN EDIT PENGGALANGAN DANA
    channel = pyqtSignal(str)
    def __init__(self):
        super().__init__()
        
        # set overall page layout
        self.setFixedSize(1440, 1024)
        self.setWindowTitle("KITASABI - Pilih Kategori Penggalangan")
        self.setStyleSheet('background-color: #F2F4F7')
        # nanti janlup connect database
        self.setWidget()
        current_directory = str(pathlib.Path(__file__).parent.absolute())
        path = current_directory + '/../../img/icon.png'
        self.setWindowIcon(QIcon(path))

    def setWidget(self):
        self.setStyleSheet('''
            QWidget {
                background-color: #E5E5E5;
            }
            QLabel {
                color: #25313C;
                background: transparent;
            }
            QLineEdit {
                background: white;
                font-size: 12px;
                padding: 0 10 0 10
            }
            QTextEdit {
                border: 0;
                background: transparent;
                font-size: 24px;
                font-weight: bold;
                color: #25313C;
            }
            QPushButton {
                color: #ffffff;
                background-color: #5A4FF3;
                border: 1px solid #5A4FF3;
                border-radius: 12px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #6b75ff;
            }
        ''')

        self.text = QLabel(self)
        self.text.setText("Pilih Kategori")
        self.text.setStyleSheet('''
            font-weight: bold;
            font-size: 38px;
        ''')
        self.text.move(591, 93)

        self.subtext = QLabel(self)
        self.subtext.setText("Ingin membuka penggalangan dana kategori apa?")
        self.subtext.setStyleSheet('''
            font-size: 22px;
        ''')
        self.subtext.move(471, 160)

        self.nonkesButton = QPushButton(self)
        self.nonkesButton.setFixedSize(402, 402)
        self.nonkesButton.move(770, 256)
        self.nonkesButton.setText("Non-Kesehatan")
        self.nonkesButton.setStyleSheet('font-size: 28px')
        self.nonkesButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.nonkesButton.clicked.connect(self.goToFormNonKesehatan)

        self.kesButton = QPushButton(self)
        self.kesButton.setFixedSize(402, 402)
        self.kesButton.move(268, 256)
        self.kesButton.setText("Kesehatan")
        self.kesButton.setStyleSheet('font-size: 28px')
        self.kesButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.kesButton.clicked.connect(self.goToFormKesehatan)

        self.returnButton = QPushButton(self)
        self.returnButton.setText("< Kembali ke Laman Utama")
        self.returnButton.setFixedSize(258, 36)
        self.returnButton.move(53, 32)
        self.returnButton.clicked.connect(self.goToHome)

    def goToHome(self):
        self.channel.emit("utama")

    def goToFormKesehatan(self):
        self.channel.emit("kesehatan")

    def goToFormNonKesehatan(self):
        self.channel.emit("nonkesehatan")


# UNCOMMENT BELOW FOR TESTING  
# app = QApplication(sys.argv)
# window = LamanPenggalangDana()
# window.show()
# sys.exit(app.exec())
