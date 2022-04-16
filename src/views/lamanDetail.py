from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QTextEdit, QPushButton
from PyQt6.QtGui import QFont, QCursor, QImage, QPixmap
from PyQt6.QtCore import Qt
import sys
import urllib.request

class LamanDetail(QWidget):
    def __init__(self):
        super().__init__()
        
        # set overall page layout
        self.setFixedSize(1440, 1024)
        self.setWindowTitle("KITASABI - Detail Penggalangan")
        self.setStyleSheet('background-color: #F2F4F7')

        # nanti janlup connect database
    
        # set fonts
        mulish16 = QFont()
        mulish16.setFamily("Mulish"); mulish16.setPixelSize(16)
        mulish24 = QFont()
        mulish24.setFamily("Mulish"); mulish24.setPixelSize(24)
        mulish44 = QFont()
        mulish44.setFamily("Mulish"); mulish44.setPixelSize(44)
        self.setWidget()

    def setWidget(self):
        # set navbar (home + profile button)
        self.navbar = QTextEdit(self)
        self.navbar.setDisabled(True)
        self.navbar.setFixedSize(1440, 95)
        self.navbar.setStyleSheet('background-color: #BBC8D4')
        self.homeButton = QPushButton(self)
        self.homeButton.setText('Kitasabi')
        self.homeButton.setStyleSheet('''
            QPushButton {
                font-size: 28px;
                padding-left: 50px;
                padding-top: 25px;
                background: transparent;
                border: 0;
                font-weight: bold;
            }
            QPushButton:hover {
                color: #FFFFFF;
            }
        ''')
        # self.homeButton.clicked.connected(go to home)
        self.profileButton = QPushButton(self)
        self.profileButton.setFixedSize(56, 56)
        self.profileButton.move(1323, 22)
        self.profileButton.setStyleSheet('''
            QPushButton {
                padding-right: 50px;
                padding-top: 25px;
                background: #DAE3EA;
                border: 2px;
                border-radius: 28;
            }
            QPushButton:hover {
                background: #FFFFFF;
            }
        ''')
        # self.profileButton.clicked.connected(go to profile edit)

        # set preview penggalangan dana
        self.previewPg = QTextEdit(self)
        self.previewPg.setDisabled(True)
        self.previewPg.setFixedSize(808, 613)
        self.previewPg.move(45, 133)
        self.previewPg.setStyleSheet('background-color: #BBC8D4')
        self.judulPg = QTextEdit(self)
        self.judulPg.setDisabled(True)
        self.judulPg.setFixedSize(754, 70)
        self.judulPg.move(72, 171)
        self.judulPg.setText("BANTU SAYA REFORMASI CIREBON")
        self.judulPg.setStyleSheet('''
            background-color: #F2F4F7; 
            padding: 20 5 5 20; 
            font-size: 16px; 
            font-weight: bold; 
            color: #25313C;
        ''')
        self.descPg = QTextEdit(self)
        self.descPg.setDisabled(True)
        self.descPg.setFixedSize(754, 225)
        self.descPg.move(72, 505)
        self.descPg.setText("Deskripsi Penggalangan Dana (ISI PAKE DATA)")
        self.descPg.setStyleSheet('padding: 10 10 10 10')
        # temporary for image
        url = 'https://yt3.ggpht.com/ytc/AKedOLQU2qqsQIYjE4SgWbHOYL4QkPO6dEXBcV8SnYEDig=s900-c-k-c0x00ffffff-no-rj'
        data = urllib.request.urlopen(url).read()

        image = QImage()
        image.loadFromData(data)

        self.imagePg = QLabel(self)
        self.imagePg.setFixedSize(754, 243)
        self.imagePg.move(72, 255)
        self.imagePg.setScaledContents(True)
        pixmap = QPixmap(image)
        self.imagePg.setPixmap(pixmap)
        
        # set timeline donatur
        self.donaturTimeline = QTextEdit(self)
        self.donaturTimeline.setDisabled(True)
        self.donaturTimeline.setFixedSize(527, 316)
        self.donaturTimeline.move(868, 133)
        self.donaturTimeline.setStyleSheet('background-color: #DAE3EA')
        self.donaturTimeline.setText("Timeline Donatur")
        self.donaturTimeline.setStyleSheet('padding: 10 10 10 10; color: #25313C; font-weight: bold; font-size: 18px')

        # set info donatur
        self.infoPenggalang = QTextEdit(self)
        self.infoPenggalang.setDisabled(True)
        self.infoPenggalang.setFixedSize(527, 293)
        self.infoPenggalang.move(868, 453)
        self.infoPenggalang.setStyleSheet('background-color: #DAE3EA')
        self.infoPenggalang.setText("Info Penggalang Dana")
        self.infoPenggalang.setStyleSheet('padding: 20 20 10 10; color: #25313C; font-weight: bold; font-size: 18px')
        self.identitas = QLabel(self)
        self.identitas.setText("Nama (ISI DATA PENGGALANG)")
        self.identitas.move(888, 523)
        self.identitas.setStyleSheet('color: #25313C; font-size: 14px')
        self.kategori = QLabel(self)
        self.kategori.setText("Kategori (ISI DATA PENGGALANG)")
        self.kategori.move(888, 563)
        self.kategori.setStyleSheet('color: #25313C; font-size: 14px')
        self.target = QLabel(self)
        self.target.setText("Target (ISI DATA PENGGALANG)")
        self.target.move(888, 603)
        self.target.setStyleSheet('color: #25313C; font-size: 14px')
        
        # set donasi button
        self.bayar = QPushButton(self)
        self.bayar.setText("BERDONASI")
        self.bayar.setFixedSize(165, 42)
        self.bayar.move(1055, 671)
        self.bayar.setStyleSheet('''
            QPushButton {
                border: 2px solid #5A4FF3;
                border-radius: 20px;
                background-color: #5A4FF3;
                padding: 10px 10px 10px 10px;
                color: white;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #FFFFFF;
                color: #5A4FF3;
            }
        ''')
        self.bayar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        # self.submitPage.clicked.connect(send)


# UNCOMMENT BELOW FOR TESTING  
# app = QApplication(sys.argv)
# window = LamanDetail()
# window.show()
# sys.exit(app.exec())
