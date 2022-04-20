from PyQt6.QtWidgets import QApplication, QWidget, QTextEdit, QPushButton, QLineEdit, QLabel
from PyQt6.QtGui import QFont, QCursor, QImage, QPixmap, QIcon
from PyQt6.QtCore import pyqtSignal, Qt
import sys, requests, json, pathlib
import urllib.request
from requests.auth import HTTPBasicAuth

class LamanEksplor(QWidget):
    channel = pyqtSignal(str, int)

    session = {
		"username-email": "",
		"password": "",
	}
    
    def setSession(self, usernameEmail, password):
        self.session["username-email"] = usernameEmail
        self.session["password"] = password

    idLaman = {
        "laman1": -1,
        "laman2": -1,
    }

    def __init__(self):
        super().__init__()
        
        # set overall page layout
        self.setFixedSize(1440, 1024)
        self.setWindowTitle("KITASABI - Eksplor")
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

        self.returnButton = QPushButton(self)
        self.returnButton.setText("< Kembali ke Laman Utama")
        self.returnButton.setFixedSize(258, 36)
        self.returnButton.move(53, 32)
        self.returnButton.clicked.connect(self.goToHome)

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
        self.profileButton.clicked.connect(self.goToEditProfil)

        # set search bar
        self.searchbar = QLineEdit(self)
        self.searchbar.setPlaceholderText("Cari Donasi")
        self.searchbar.setFixedSize(270, 42)
        self.searchbar.move(970, 81)
        self.searchbar.returnPressed.connect(self.search)

        # set preview penggalangan dana
        self.previewBg1 = QTextEdit(self)
        self.previewBg1.setDisabled(True)
        self.previewBg1.setFixedSize(1010, 227)
        self.previewBg1.move(233, 212)
        self.previewBg1.setStyleSheet('background-color: #FFFFFF')
       
        self.previewText1 = QTextEdit(self)
        self.previewText1.setDisabled(True)
        self.previewText1.setFixedSize(500, 130)
        self.previewText1.move(469, 262)

        self.previewImg1 = QLabel(self)
        self.previewImg1.setFixedSize(176, 176)
        self.previewImg1.move(268, 238)
        self.previewImg1.setScaledContents(True)

        # set bayar button
        self.detail1 = QPushButton(self)
        self.detail1.setText("Lihat Detail >")
        self.detail1.setFixedSize(165, 52)
        self.detail1.move(1020, 301)
        self.detail1.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.detail1.clicked.connect(self.goToLamanDetail1)

        # set preview penggalangan dana
        self.previewBg2 = QTextEdit(self)
        self.previewBg2.setDisabled(True)
        self.previewBg2.setFixedSize(1010, 227)
        self.previewBg2.move(233, 462)
        self.previewBg2.setStyleSheet('background-color: #FFFFFF')
        
        self.previewText2 = QTextEdit(self)
        self.previewText2.setFixedSize(500, 130)
        self.previewText2.setDisabled(True)
        self.previewText2.setText("Judul Penggalangan (ISI PAKE DATA)")
        self.previewText2.move(469, 512)

        self.previewImg2 = QLabel(self)
        self.previewImg2.setFixedSize(176, 176)
        self.previewImg2.move(268, 488)
        self.previewImg2.setScaledContents(True)

        # set bayar button
        self.detail2 = QPushButton(self)
        self.detail2.setText("Lihat Detail >")
        self.detail2.setFixedSize(165, 52)
        self.detail2.move(1020, 551)
        self.detail2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.detail2.clicked.connect(self.goToLamanDetail2)
    
    def setLaman(self):
        response = requests.get('http://localhost:3000/laman/eksplor-total-donasi',
            auth=HTTPBasicAuth(self.session["username-email"], self.session["password"])
        )
        if (response.status_code == 200):
            # get list of laman (dictionary)
            listRes = json.loads(response.text)
            # get laman 1
            dictRes1 = (listRes[0])
            # set id laman
            self.idLaman["laman1"] = dictRes1["id-laman"]
            # set judul
            self.previewText1.setText(str(dictRes1["judul"]))
            # set image
            url = dictRes1["foto-laman"][0][0]
            data = urllib.request.urlopen(url).read()
            image = QImage()
            image.loadFromData(data)
            pixmap = QPixmap(image)
            self.previewImg1.setPixmap(pixmap)
            # check for laman 2
            if (len(listRes) >= 2):
                # get laman 2
                dictRes2 = (listRes[1])
                # set id laman
                self.idLaman["laman2"] = dictRes2["id-laman"]
                # set judul
                self.previewText2.setText(dictRes2["judul"])
                # set image
                url = dictRes2["foto-laman"][0][0]
                data = urllib.request.urlopen(url).read()
                image = QImage()
                image.loadFromData(data)
                pixmap = QPixmap(image)
                self.previewImg2.setPixmap(pixmap)
                return True
            else:
                # placeholder data
                self.previewText2.setText("Placeholder Title")
                url = 'https://yt3.ggpht.com/ytc/AKedOLQU2qqsQIYjE4SgWbHOYL4QkPO6dEXBcV8SnYEDig=s900-c-k-c0x00ffffff-no-rj'
                data = urllib.request.urlopen(url).read()
                image = QImage()
                image.loadFromData(data)
                pixmap = QPixmap(image)
                self.previewImg2.setPixmap(pixmap)
                return False
        else:
            # placeholder data
            self.previewText1.setText("Placeholder Title")
            url = 'https://yt3.ggpht.com/ytc/AKedOLQU2qqsQIYjE4SgWbHOYL4QkPO6dEXBcV8SnYEDig=s900-c-k-c0x00ffffff-no-rj'
            data = urllib.request.urlopen(url).read()
            image = QImage()
            image.loadFromData(data)
            pixmap = QPixmap(image)
            self.previewImg1.setPixmap(pixmap)
            return False

    def search(self):
        # self.previewText1.setText(self.searchbar.text())
        # self.previewText2.setText(self.searchbar.text())

        response = requests.get('http://localhost:3000/laman/search-laman', data={"query-judul": self.searchbar.text()} ,
            auth=HTTPBasicAuth(self.session["username-email"], self.session["password"])
        )

        if (response.status_code == 200):
            # get list of laman (dictionary)
            listRes = json.loads(response.text)
            # get laman 1
            dictRes1 = (listRes[0])
            # set id laman
            self.idLaman["laman1"] = dictRes1["id-laman"]
            # set judul
            self.previewText1.setText(str(dictRes1["judul"]))
            # set image
            url = dictRes1["foto-laman"][0][0]
            data = urllib.request.urlopen(url).read()
            image = QImage()
            image.loadFromData(data)
            pixmap = QPixmap(image)
            self.previewImg1.setPixmap(pixmap)
            # check for laman 2
            if (len(listRes) >= 2):
                # get laman 2
                dictRes2 = (listRes[1])
                # set id laman
                self.idLaman["laman2"] = dictRes2["id-laman"]
                # set judul
                self.previewText2.setText(dictRes2["judul"])
                # set image
                url = dictRes2["foto-laman"][0][0]
                data = urllib.request.urlopen(url).read()
                image = QImage()
                image.loadFromData(data)
                pixmap = QPixmap(image)
                self.previewImg2.setPixmap(pixmap)
            else:
                # placeholder data
                self.previewText2.setText("Placeholder Title")
                url = 'https://yt3.ggpht.com/ytc/AKedOLQU2qqsQIYjE4SgWbHOYL4QkPO6dEXBcV8SnYEDig=s900-c-k-c0x00ffffff-no-rj'
                data = urllib.request.urlopen(url).read()
                image = QImage()
                image.loadFromData(data)
                pixmap = QPixmap(image)
                self.previewImg2.setPixmap(pixmap)
        else:
            # placeholder data
            self.previewText1.setText("Placeholder Title")
            self.previewText2.setText("Placeholder Title")
            url = 'https://yt3.ggpht.com/ytc/AKedOLQU2qqsQIYjE4SgWbHOYL4QkPO6dEXBcV8SnYEDig=s900-c-k-c0x00ffffff-no-rj'
            data = urllib.request.urlopen(url).read()
            image = QImage()
            image.loadFromData(data)
            pixmap = QPixmap(image)
            self.previewImg1.setPixmap(pixmap)
            self.previewImg2.setPixmap(pixmap)
        self.searchbar.clear()

        
    def goToHome(self):
        self.channel.emit("home", -1)
        
    def goToEditProfil(self):
        self.channel.emit("profile", -1)

    def goToLamanDetail1(self):
        self.channel.emit("detail", self.idLaman["laman1"])
    
    def goToLamanDetail2(self):
        self.channel.emit("detail", self.idLaman["laman2"])

# UNCOMMENT BELOW FOR TESTING  
# app = QApplication(sys.argv)
# window = LamanEksplor()
# window.show()
# sys.exit(app.exec())

