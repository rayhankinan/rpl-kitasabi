from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QTextEdit, QPushButton
from PyQt6.QtGui import QFont, QCursor, QImage, QPixmap, QIcon
from PyQt6.QtCore import pyqtSignal
from PyQt6.QtCore import Qt
import urllib.request
import sys, requests, json, pathlib
from requests.auth import HTTPBasicAuth

class LamanDetail(QWidget):
    channel = pyqtSignal(str, int)

    session = {
		"username-email": "",
		"password": "",
	}
    
    def setSession(self, usernameEmail, password):
        self.session["username-email"] = usernameEmail
        self.session["password"] = password

    idLaman = {
        "id-laman": -1
    }

    def __init__(self):
        super().__init__()
        
        # set overall page layout
        self.setFixedSize(1440, 1024)
        self.setWindowTitle("KITASABI - Detail Penggalangan")
        self.setStyleSheet('background-color: #F2F4F7')
        current_directory = str(pathlib.Path(__file__).parent.absolute())
        path = current_directory + '/../../img/icon.png'
        self.setWindowIcon(QIcon(path))
    
        # set fonts
        mulish16 = QFont()
        mulish16.setFamily("Mulish"); mulish16.setPixelSize(16)
        mulish24 = QFont()
        mulish24.setFamily("Mulish"); mulish24.setPixelSize(24)
        mulish44 = QFont()
        mulish44.setFamily("Mulish"); mulish44.setPixelSize(44)
        self.setWidget()

    def setWidget(self):
        self.setStyleSheet('''
            QWidget {
                background-color: #E5E5E5;
            }
            QLabel {
                color: #25313C;
                font-weight: extra-bold;
                background: transparent;
            }
            QTextEdit {
                background-color: #F2F4F7; 
                padding: 20 5 5 20; 
                font-size: 16px; 
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
        self.homeButton.clicked.connect(self.goToHome)

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
        self.profileButton.clicked.connect(self.goToEditProfile)

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

        self.descPg = QTextEdit(self)
        self.descPg.setDisabled(True)
        self.descPg.setFixedSize(754, 225)
        self.descPg.move(72, 485)
        self.descPg.setStyleSheet('padding: 10 10 10 10')

        self.imagePg = QLabel(self)
        self.imagePg.setFixedSize(754, 228)
        self.imagePg.move(72, 248)
        self.imagePg.setScaledContents(True)
        
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
        self.infoPenggalang.setText("Info Penggalangan Dana")
        self.infoPenggalang.setStyleSheet('padding: 20 20 10 10; color: #25313C; font-weight: bold; font-size: 18px')
        
        self.deadline = QLabel(self)
        self.deadline.move(888, 523)
        self.deadline.setStyleSheet('color: #25313C; font-size: 14px')

        self.kategori = QLabel(self)
        self.kategori.move(888, 563)
        self.kategori.setStyleSheet('color: #25313C; font-size: 14px')

        self.target = QLabel(self)
        self.target.move(888, 603)
        self.target.setStyleSheet('color: #25313C; font-size: 14px')
        
        # set donasi button
        self.bayar = QPushButton(self)
        self.bayar.setText("BERDONASI")
        self.bayar.setFixedSize(165, 42)
        self.bayar.move(1055, 671)
        self.bayar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.bayar.clicked.connect(self.goToLamanPembayaran)
    
    def setLaman(self, idLaman):
        # set id laman
        self.idLaman["id-laman"] = idLaman
        response = requests.get('http://localhost:3000/laman/detail-laman', data=self.idLaman,
            auth=HTTPBasicAuth(self.session["username-email"], self.session["password"])
        )
        if (response.status_code == 200):
            # get list of laman (dictionary)
            listRes = json.loads(response.text)
            # set judul
            self.judulPg.setText(listRes["judul"])
            # set deskripsi
            self.descPg.setText(listRes["deskripsi"])
            # set image
            url = listRes["foto-laman"][0][0]
            data = urllib.request.urlopen(url).read()
            image = QImage()
            image.loadFromData(data)
            pixmap = QPixmap(image)
            self.imagePg.setPixmap(pixmap)
            # set kategori
            self.kategori.setText(listRes["kategori"])
            # set target
            self.target.setText(str(listRes["target"]))
            # set deadline
            self.deadline.setText(listRes["timestamp"])
            return True
        else:
            self.judulPg.setText("BANTU SAYA REFORMASI CIREBON")
            self.descPg.setText("Deskripsi Penggalangan Dana (ISI PAKE DATA)")
            url = 'https://yt3.ggpht.com/ytc/AKedOLQU2qqsQIYjE4SgWbHOYL4QkPO6dEXBcV8SnYEDig=s900-c-k-c0x00ffffff-no-rj'
            data = urllib.request.urlopen(url).read()
            image = QImage()
            image.loadFromData(data)
            pixmap = QPixmap(image)
            self.imagePg.setPixmap(pixmap)
            self.kategori.setText("Kategori (ISI DATA PENGGALANG)")
            self.target.setText("Target (ISI DATA PENGGALANG)")
            return False

    def goToHome(self):
        self.channel.emit("home", -1)
        
    def goToEditProfile(self):
        self.channel.emit("profile", -1)

    def goToLamanPembayaran(self):
        self.channel.emit("pembayaran", self.idLaman["id-laman"])

# UNCOMMENT BELOW FOR TESTING  
# app = QApplication(sys.argv)
# window = LamanDetail()
# window.show()
# sys.exit(app.exec())
