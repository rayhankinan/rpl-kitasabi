from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton
from PyQt6.QtGui import QCursor
from PyQt6.QtCore import pyqtSignal, Qt
from views.formKesehatan import FormKesehatan
from views.formNonKesehatan import FormNonKesehatan
import sys

class LamanPenggalangDana(QWidget):
    channel = pyqtSignal(str)
    def __init__(self):
        super().__init__()
        
        # set overall page layout
        self.setFixedSize(1440, 1024)
        self.setWindowTitle("KITASABI - Pilih Kategori Penggalangan")
        self.setStyleSheet('background-color: #F2F4F7')
        # nanti janlup connect database
        self.setWidget()

    def setWidget(self):
        self.text = QLabel(self)
        self.text.setText("Pilih Kategori")
        self.text.setStyleSheet('''
            color: #25313C;
            font-weight: bold;
            font-size: 38px;
        ''')
        self.text.move(591, 93)

        self.subtext = QLabel(self)
        self.subtext.setText("Ingin membuka penggalangan dana kategori apa?")
        self.subtext.setStyleSheet('''
            color: #25313C;
            font-size: 22px;
        ''')
        self.subtext.move(471, 160)

        self.nonkesButton = QPushButton(self)
        self.nonkesButton.setFixedSize(402, 402)
        self.nonkesButton.move(770, 266)
        self.nonkesButton.setText("NON-KESEHATAN")
        self.nonkesButton.setStyleSheet('''
            QPushButton {
                background: #5A4FF3;
                border: 2px solid #5A4FF3;
                border-radius: 200px;
                color: white;
                font-weight: bold;
                font-size: 28px;
            }
            QPushButton:hover {
                background: #FFFFFF;
                color: #5A4FF3;
            }
        ''')
        self.nonkesButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.nonkesButton.clicked.connect(self.goToFormNonKesehatan)

        self.kesButton = QPushButton(self)
        self.kesButton.setFixedSize(402, 402)
        self.kesButton.move(268, 266)
        self.kesButton.setText("KESEHATAN")
        self.kesButton.setStyleSheet('''
            QPushButton {
                background: #5A4FF3;
                border: 2px solid #5A4FF3;
                border-radius: 200px;
                color: white;
                font-weight: bold;
                font-size: 28px;
            }
            QPushButton:hover {
                background: #FFFFFF;
                color: #5A4FF3;
            }
        ''')
        self.kesButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.kesButton.clicked.connect(self.goToFormKesehatan)

    def goToFormKesehatan(self):
        self.channel.emit("kesehatan")

    def goToFormNonKesehatan(self):
        self.channel.emit("nonkesehatan")


# UNCOMMENT BELOW FOR TESTING  
# app = QApplication(sys.argv)
# window = LamanPenggalangDana()
# window.show()
# sys.exit(app.exec())
