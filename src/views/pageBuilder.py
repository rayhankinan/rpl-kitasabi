from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QTextEdit, QPushButton, QFileDialog, QCalendarWidget, QHBoxLayout, QMessageBox
from PyQt6.QtGui import QFont, QCursor
from PyQt6.QtCore import Qt, QDate, pyqtSignal
import sys
import requests
from requests.auth import HTTPBasicAuth

class PageBuilder(QWidget):
    channel = pyqtSignal()

    session = {
		"username-email": "",
		"password": "",
	}
    
    def setSession(self, usernameEmail, password):
        self.session["username-email"] = usernameEmail
        self.session["password"] = password

    dataText = {
        "deadline": ""
    }

    dataFile = {
        "foto-laman": ""
    }

    def __init__(self):
        super().__init__()
        
        # set overall page layout
        self.setFixedSize(1440, 1024)
        self.setWindowTitle("KITASABI - Page Builder")
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
        self.setStyleSheet('''
            QWidget {
                background-color: #E5E5E5;
            }
            QLabel {
                color: #25313C;
                font-weight: bold;
                font-size: 38px;
            }
            QTextEdit, QLineEdit {
                padding: 11px 30px 11px 30px;
                border: 1px solid rgba(90, 79, 243, 1);
                border-radius: 5px;
                color: rgba(37, 49, 60, 1);
                background-color: #FFFFFF;
            }
            QPushButton {
                color: #ffffff;
                background-color: #5A4FF3;
                border: 1px solid #5A4FF3;
                border-radius: 20px;
            }
            QPushButton:hover {
                background-color: #6b75ff;
            }
        ''')
        # set page title label
        text = QLabel(self)
        text.setText("Pembuatan Laman Penggalangan Dana")
        text.move(359, 53)

        # set fixed judul box
        self.judulFixed = QLineEdit(self)
        self.judulFixed.setEnabled(False)
        self.judulFixed.setPlaceholderText("Kategori: Kesehatan")
        self.judulFixed.setFixedSize(427, 47)
        self.judulFixed.move(481, 142)

        # set fixed judul box
        self.judulFixed = QLineEdit(self)
        self.judulFixed.setEnabled(False)
        self.judulFixed.setPlaceholderText("Judul: tolong keluarga ini membeli beras (ISI PAKE DATA DR DATABASE)")
        self.judulFixed.setFixedSize(427, 47)
        self.judulFixed.move(481, 208)

        # set upload foto box
        self.uploadFoto = QPushButton(self)
        self.uploadFoto.setText("Upload Foto")
        self.uploadFoto.setFixedSize(427, 47)
        self.uploadFoto.move(481, 521)
        self.uploadFoto.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.uploadFoto.clicked.connect(self.openFile)

        # set fixed deskripsi box
        self.descFixed = QTextEdit(self)
        self.descFixed.setEnabled(False)
        self.descFixed.setPlaceholderText("Deskripsi: ibu jubaidah dan anaknya ilham ingin membeli beras tolonglah mereka membeli segelintir beras (ISI PAKE DATA DR DATABASE)")
        self.descFixed.setFixedSize(427, 163)
        self.descFixed.move(481, 339)

        # set fixed target donasi box
        self.targetFixed = QLineEdit(self)
        self.targetFixed.setEnabled(False)
        self.targetFixed.setPlaceholderText("Target: 10 juta (ISI PAKE DATA DR DATABASE)")
        self.targetFixed.setFixedSize(427, 47)
        self.targetFixed.move(481, 274)

        # set date picker box
        self.setDeadline = QPushButton(self)
        self.setDeadline.setText("Pilih Tenggat Waktu")
        self.setDeadline.setFixedSize(427, 47)
        self.setDeadline.move(481, 586)
        self.setDeadline.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.setDeadline.clicked.connect(self.pickDate)

        # set submit button
        self.submitPage = QPushButton(self)
        self.submitPage.setText("SUBMIT")
        self.submitPage.setFixedSize(165, 52)
        self.submitPage.move(603, 664)
        self.submitPage.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.submitPage.clicked.connect(self.goToRiwayatPenggalang)

    def resetState(self):
        self.dataText["deadline"] = ""
        self.dataFile["foto-laman"] = ""

    def sendData(self):
        response = requests.post('http://localhost:3000/laman/create-laman', data=self.dataText, files=self.dataFile,
            auth=HTTPBasicAuth(self.session["username-email"], self.session["password"])
        )
        if (response.status_code == 201):
            return True
        else:
            return False

    def goToRiwayatPenggalang(self):
        success = self.sendData()
        if (success):
            self.resetState()
            self.channel.emit()
        else:
            msgBox = QMessageBox()
            msgBox.setText("<p>Please fill out the form properly!</p>")
            msgBox.setWindowTitle("Request Permintaan Failed")
            msgBox.setIcon(QMessageBox.Icon.Warning)
            msgBox.setStyleSheet("background-color: white")
            msgBox.setStandardButtons(QMessageBox.StandardButton.Ok)
            msgBox.exec()
            return

    # get jpg file
    def openFile(self):
        file = QFileDialog.getOpenFileName(self, 'Open a file', '', 'Image (*.jpg*)')
        if file != ('', ''):
            path = file[0]
            self.dataFile[type] = open(path, "rb")
            
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
        self.dataText["deadline"] = date.toString()


# # UNCOMMENT BELOW FOR TESTING  
# app = QApplication(sys.argv)
# window = PageBuilder()
# window.show()
# sys.exit(app.exec())
