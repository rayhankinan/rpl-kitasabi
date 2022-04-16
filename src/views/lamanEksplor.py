from PyQt6.QtWidgets import QApplication, QWidget, QTextEdit, QPushButton, QLineEdit, QLabel
from PyQt6.QtGui import QFont, QCursor, QImage, QPixmap
from PyQt6.QtCore import Qt
import sys
import urllib.request


class LamanEksplor(QWidget):
    def __init__(self):
        super().__init__()
        
        # set overall page layout
        self.setFixedSize(1440, 1024)
        self.setWindowTitle("KITASABI - Pembayaran")
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
        self.returnButton = QPushButton(self)
        self.returnButton.setText("< Kembali ke Laman Utama")
        self.returnButton.setFixedSize(258, 36)
        self.returnButton.move(53, 32)
        self.returnButton.setStyleSheet('''
            QPushButton {
                padding-left: 2px;
                background: #5A4FF3;
                border: 1px solid #5A4FF3;
                color: white;
                border-radius: 28;
                font-weight: bold;
            }
            QPushButton:hover {
                background: #FFFFFF;
                color: black;
            }
        ''')
        # self.returnButton.clicked.connected(go to laman utama)

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

        # set search bar
        self.searchbar = QLineEdit(self)
        self.searchbar.setPlaceholderText("Cari Donasi")
        self.searchbar.setFixedSize(270, 42)
        self.searchbar.move(970, 81)
        self.searchbar.setStyleSheet('''
            background: white;
            font-size: 12px;
            padding: 0 10 0 10
        ''')
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
        self.previewText1.setText("Judul Penggalangan (ISI PAKE DATA)")
        self.previewText1.move(469, 262)
        self.previewText1.setStyleSheet('''
            border: 0;
            background: transparent;
            font-size: 24px;
            font-weight: bold;
            color: #25313C;
        ''')
        # temporary for image
        url1 = 'https://pbs.twimg.com/profile_images/631884742896431104/RMnmakF-_400x400.jpg'
        data1 = urllib.request.urlopen(url1).read()

        image1 = QImage()
        image1.loadFromData(data1)

        self.previewImg1 = QLabel(self)
        self.previewImg1.setFixedSize(176, 176)
        self.previewImg1.move(268, 238)
        self.previewImg1.setScaledContents(True)
        pixmap1 = QPixmap(image1)
        self.previewImg1.setPixmap(pixmap1)


        # set bayar button
        self.bayar1 = QPushButton(self)
        self.bayar1.setText("Lihat Detail >")
        self.bayar1.setFixedSize(165, 52)
        self.bayar1.move(1020, 301)
        self.bayar1.setStyleSheet('''
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
        self.bayar1.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        # self.submitPage.clicked.connect(send)

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
        self.previewText2.setStyleSheet('''
            border: 0;
            background: transparent;
            font-size: 24px;
            font-weight: bold;
            color: #25313C;
        ''')
        # temporary for image
        url2 = 'https://pbs.twimg.com/profile_images/631884742896431104/RMnmakF-_400x400.jpg'
        data2 = urllib.request.urlopen(url2).read()

        image2 = QImage()
        image2.loadFromData(data2)

        self.previewImg2 = QLabel(self)
        self.previewImg2.setFixedSize(176, 176)
        self.previewImg2.move(268, 488)
        self.previewImg2.setScaledContents(True)
        pixmap2 = QPixmap(image2)
        self.previewImg2.setPixmap(pixmap2)

        # set bayar button
        self.bayar2 = QPushButton(self)
        self.bayar2.setText("Lihat Detail >")
        self.bayar2.setFixedSize(165, 52)
        self.bayar2.move(1020, 551)
        self.bayar2.setStyleSheet('''
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
        self.bayar2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        # self.submitPage.clicked.connect(send)

    def search(self):
        print("yoyo")
        self.previewText1.setText(self.searchbar.text())
        self.previewText2.setText(self.searchbar.text())
        self.searchbar.clear()
        

# UNCOMMENT BELOW FOR TESTING  
# app = QApplication(sys.argv)
# window = LamanEksplor()
# window.show()
# sys.exit(app.exec())
