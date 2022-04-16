from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QTextEdit, QPushButton, QFileDialog, QCalendarWidget, QHBoxLayout, QLineEdit, QComboBox
from PyQt6.QtGui import QFont, QCursor
from PyQt6.QtCore import Qt, QDate
import sys

class LamanPembayaran(QWidget):
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

        # set return button (to laman penggalangan dana)
        self.returnButton = QPushButton(self)
        self.returnButton.setText("< Kembali ke Laman Penggalangan Dana")
        self.returnButton.setFixedSize(308, 36)
        self.returnButton.move(54, 120)
        self.returnButton.setStyleSheet('''
            QPushButton {
                padding-left: 2px;
                background: #FFFFFF;
                border: 1px solid #5A4FF3;
                border-radius: 28;
            }
            QPushButton:hover {
                background: #5A4FF3;
            }
        ''')
        # self.returnButton.clicked.connected(go to home)

        # set preview penggalangan dana
        self.previewBg = QTextEdit(self)
        self.previewBg.setDisabled(True)
        self.previewBg.setFixedSize(1010, 227)
        self.previewBg.move(233, 212)
        self.previewBg.setStyleSheet('background-color: #BBC8D4')
        self.previewText = QLabel(self)
        self.previewText.setText("Preview (ISI PAKE DATA)")
        self.previewText.move(559, 262)
        self.previewText.setStyleSheet('''
            background: transparent;
            font-size: 24px;
            font-weight: bold;
            color: #25313C;
        ''')
        self.targetBg = QTextEdit(self)
        self.targetBg.setDisabled(True)
        self.targetBg.setFixedSize(603, 61)
        self.targetBg.move(550, 339)
        self.targetBg.setStyleSheet('background-color: #94A3B1')
        self.targetText = QLabel(self)
        self.targetText.setText("Target (ISI PAKE DATA)")
        self.targetText.move(579, 350)
        self.targetText.setStyleSheet('''
            background: transparent;
            font-size: 24px;
            color: #25313C;
        ''')
        # temporary for image
        self.previewImg = QTextEdit(self)
        self.previewImg.setText('ISI PAKE DATA')
        self.previewImg.setDisabled(True)
        self.previewImg.setFixedSize(190, 176)
        self.previewImg.move(278, 243)
        self.previewImg.setStyleSheet('background-color: #94A3B1; color: black;')

        # set input nominal box
        self.nominal = QLineEdit(self)
        self.nominal.setFixedSize(1010, 91)
        self.nominal.move(233, 493)
        self.nominal.setPlaceholderText('10000000 (contoh penulisan)')
        self.nominal.setStyleSheet('background-color: #FFFFFF; border: 1px solid #5A4FF3; padding: 30 20 20 50; font-size: 16px')
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
            }
            QPushButton:hover {
                background-color: #FFFFFF;
                color: #5A4FF3;
            }
        ''')
        self.bayar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        # self.submitPage.clicked.connect(send)


        

    # get jpg file
    def openFile(self):
        file = QFileDialog.getOpenFileName(self, 'Open a file', '', 'Image (*.jpg*)')
        if file != ('', ''):
            path = file[0]
            print(path)
            # TEST OPEN TXT FILE
            # with open(path, "r") as f:
            #     print(f.readline())
            
    # get date
    def pickDate(self):
        # date picker
        self.cal = QCalendarWidget(self)
        self.cal.setGridVisible(True)
        self.cal.clicked[QDate].connect(self.setDate)
        
        # pop up calendar view
        self.calendarWindow = QWidget()
        viewbox = QHBoxLayout()
        viewbox.addWidget(self.cal)
        self.calendarWindow.setLayout(viewbox)
        self.calendarWindow.setGeometry(300, 300, 415, 350)
        self.calendarWindow.setWindowTitle('Pilih Tanggal')
        self.calendarWindow.show()

    # set input as selected date
    def setDate(self, date):
        self.setDeadline.setText(date.toString())


# UNCOMMENT BELOW FOR TESTING  
app = QApplication(sys.argv)
window = LamanPembayaran()
window.show()
sys.exit(app.exec())
