from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QTextEdit, QPushButton, QLineEdit, QComboBox, QMessageBox
from PyQt6.QtGui import QFont, QCursor, QImage, QPixmap
from PyQt6.QtCore import pyqtSignal
from PyQt6.QtCore import Qt
import sys, requests, json
import urllib.request
from requests.auth import HTTPBasicAuth

class LamanPembayaran(QWidget):
    channel = pyqtSignal(str)

    session = {
		"username-email": "",
		"password": "",
	}
    
    def setSession(self, usernameEmail, password):
        self.session["username-email"] = usernameEmail
        self.session["password"] = password

    dataText = {
        "id-laman": "",
        "jumlah-transaksi": "",
    }

    def __init__(self):
        super().__init__()
        
        # set overall page layout
        self.setFixedSize(1440, 1024)
        self.setWindowTitle("KITASABI - Pembayaran")
        self.setStyleSheet('background-color: #F2F4F7')
    
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
                background: transparent;
                color: #25313C;
            }
            QLineEdit {
                background: white;
                font-size: 12px;
                padding: 0 10 0 10
            }
            QTextEdit {
                background: #BBC8D4;
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
            QComboBox {
                border: 1px solid #5A4FF3;
                background: white;
                padding-left: 10;
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

        # self.homeButton.clicked.connect(go to home)
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

        # set return button (to laman penggalangan dana)
        self.returnButton = QPushButton(self)
        self.returnButton.setText("< Kembali ke Laman Utama")
        self.returnButton.setFixedSize(268, 36)
        self.returnButton.move(233, 140)
        self.returnButton.clicked.connect(self.goToHome)

        # set preview penggalangan dana
        self.previewBg = QTextEdit(self)
        self.previewBg.setDisabled(True)
        self.previewBg.setFixedSize(1010, 227)
        self.previewBg.move(233, 212)
        self.previewBg.setStyleSheet('background-color: #BBC8D4')
        
        self.previewText = QLabel(self)
        self.previewText.move(559, 262)
        self.previewText.setStyleSheet('font-weight: bold; font-size: 24px')

        self.targetBg = QTextEdit(self)
        self.targetBg.setDisabled(True)
        self.targetBg.setFixedSize(603, 61)
        self.targetBg.move(550, 339)
        self.targetBg.setStyleSheet('background-color: #94A3B1')

        self.targetText = QLabel(self)
        self.targetText.move(579, 360)

        self.previewImg = QLabel(self)
        self.previewImg.setFixedSize(190, 176)
        self.previewImg.move(278, 243)
        self.previewImg.setScaledContents(True)

        # set input nominal box
        self.nominal = QLineEdit(self)
        self.nominal.setFixedSize(1010, 91)
        self.nominal.move(233, 493)
        self.nominal.setPlaceholderText('10000000 (contoh penulisan)')
        self.nominal.setStyleSheet('background-color: #FFFFFF; border: 1px solid #5A4FF3; padding: 30 20 20 50; font-size: 16px')
        self.nominal.textChanged.connect(self.setNominal)
        
        self.nominalText = QLabel(self)
        self.nominalText.move(243, 503)
        self.nominalText.setText("Nominal uang yang akan didonasikan:")
        self.nominalText.setStyleSheet('background: transparent; color: #ACACAC')
        
        self.nominalRp = QLabel(self)
        self.nominalRp.move(243, 493)
        self.nominalRp.setText("Rp.")
        self.nominalRp.setStyleSheet('padding-top: 40; background: transparent; color: #ACACAC; font-size: 16px;')

        # set jenis pembayaran dropdown
        self.jenis = QComboBox(self)
        self.jenis.setFixedSize(320, 36)
        self.jenis.move(233, 598)
        self.jenis.addItems(['GoPey', 'UVU', 'Virtual Account (Bank)'])
        self.jenis.setPlaceholderText('Pilih jenis pembayaran')
        self.jenis.setStyleSheet('''
            border: 1px solid #5A4FF3;
            background: white;
            padding-left: 10;
        ''')
        self.jenis.setCurrentIndex(-1)
        
        # set bayar button
        self.bayar = QPushButton(self)
        self.bayar.setText("BAYAR")
        self.bayar.setFixedSize(165, 52)
        self.bayar.move(1080, 661)
        self.bayar.setStyleSheet('''
            QPushButton {
                border: 2px solid #5A4FF3;
                border-radius: 20px;
                background-color: #5A4FF3;
                padding: 10px 10px 10px 10px;
                color: white;
                font-weight: bold;
                font-size: 16px;
            }
            QPushButton:hover {
                background-color: #FFFFFF;
                color: #5A4FF3;
            }
        ''')
        self.bayar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.bayar.clicked.connect(self.goToRiwayatDonasi)
    
    def setLaman(self, idLaman):
        self.dataText["id-laman"] = idLaman
        response = requests.get('http://localhost:3000/laman/detail-laman', data={"id-laman": idLaman},
            auth=HTTPBasicAuth(self.session["username-email"], self.session["password"])
        )
        if (response.status_code == 200):
            # get list of laman (dictionary)
            listRes = json.loads(response.text)
            # set judul
            self.previewText.setText(listRes["judul"])
            # set image
            url = listRes["foto-laman"][0][0]
            data = urllib.request.urlopen(url).read()
            image = QImage()
            image.loadFromData(data)
            pixmap = QPixmap(image)
            self.previewImg.setPixmap(pixmap)
            # set target
            self.targetText.setText(str(listRes["target"]))
            return True
        else:
            self.previewText.setText("Placeholder Title")
            url = 'https://yt3.ggpht.com/ytc/AKedOLQU2qqsQIYjE4SgWbHOYL4QkPO6dEXBcV8SnYEDig=s900-c-k-c0x00ffffff-no-rj'
            data = urllib.request.urlopen(url).read()
            image = QImage()
            image.loadFromData(data)
            pixmap = QPixmap(image)
            self.previewImg.setPixmap(pixmap)
            self.targetText.setText("Placeholder Target")
            return False
    
    def setNominal(self):
        self.dataText["jumlah-transaksi"] = self.nominal.text()

    def resetState(self):
        self.nominal.clear()
        self.jenis.clear()
        for key in list(self.dataText.keys()):
            self.dataText[key] = ""
    
    def sendData(self):
        response = requests.post('http://localhost:3000/transaksi/bayar', data=self.dataText,
            auth=HTTPBasicAuth(self.session["username-email"], self.session["password"])
        )
        if (response.status_code == 201):
            return True
        else:
            return False

    def goToHome(self):
        self.resetState()
        self.channel.emit("home")
        
    def goToEditProfile(self):
        self.resetState()
        self.channel.emit("profile")

    def goToRiwayatDonasi(self):
        success = self.sendData()
        if (success):
            self.resetState()
            self.channel.emit("riwayat")
        else:
            msgBox = QMessageBox()
            msgBox.setText("<p>Please fill out the form properly!</p>")
            msgBox.setWindowTitle("Pembayaran Failed")
            msgBox.setIcon(QMessageBox.Icon.Warning)
            msgBox.setStyleSheet("background-color: white")
            msgBox.setStandardButtons(QMessageBox.StandardButton.Ok)
            msgBox.exec()
            return

# UNCOMMENT BELOW FOR TESTING  
# app = QApplication(sys.argv)
# window = LamanPembayaran()
# window.show()
# sys.exit(app.exec())

