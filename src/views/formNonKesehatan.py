from PyQt6.QtWidgets import QApplication, QLabel, QPushButton, QTextEdit, QWidget, QMessageBox
from PyQt6.QtGui import QCursor
from PyQt6.QtCore import Qt, pyqtSignal
import requests
from requests.auth import HTTPBasicAuth
import sys

class FormNonKesehatan(QWidget):
    channel = pyqtSignal()

    session = {
		"username-email": "",
		"password": "",
	}
    
    def setSession(self, usernameEmail, password):
        self.session["username-email"] = usernameEmail
        self.session["password"] = password

    dataText = {
        "judul": "",
        "deskripsi": "",
        "target": "",
        "instansi": "",
        "akun-instagram": "",
        "akun-twitter": "",
        "akun-facebook": "",
        "nama-penerima": "",
    }
    
    def __init__(self):
        super().__init__()
        
        # set overall page layout
        self.setFixedSize(1440, 1024)
        self.setWindowTitle("KITASABI - Form Penggalangan Dana Non-Kesehatan")
        self.setStyleSheet('background-color: #F2F4F7')
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
            QTextEdit {
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
        self.text = QLabel(self)
        self.text.setText("Form Non-Kesehatan")
        self.text.move(561, 88)

        # LEFTSIDE
        # set judul
        self.judul = QTextEdit(self)
        self.judul.setPlaceholderText("Judul")
        self.judul.setFixedSize(320, 46)
        self.judul.move(336, 219)
        self.judul.textChanged.connect(self.setJudul)

        # set nama
        self.namaPenerima = QTextEdit(self)
        self.namaPenerima.setPlaceholderText("Nama Penerima")
        self.namaPenerima.setFixedSize(320, 46)
        self.namaPenerima.move(336, 279)
        self.namaPenerima.textChanged.connect(self.setNamaPenerima)

        # set fb
        self.fb = QTextEdit(self)
        self.fb.setPlaceholderText("Facebook")
        self.fb.setFixedSize(320, 46)
        self.fb.move(336, 339)
        self.fb.textChanged.connect(self.setFb)

        # set ig
        self.ig = QTextEdit(self)
        self.ig.setPlaceholderText("Instagram")
        self.ig.setFixedSize(320, 46)
        self.ig.move(336, 409)
        self.ig.textChanged.connect(self.setIg)

        # RIGHTSIDE
        # set twitter
        self.twitter = QTextEdit(self)
        self.twitter.setPlaceholderText("Twitter")
        self.twitter.setFixedSize(320, 46)
        self.twitter.move(773, 219)
        self.twitter.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.twitter.textChanged.connect(self.setTwitter)
        
        # set nama penerima
        self.namaPenerima = QTextEdit(self)
        self.namaPenerima.setPlaceholderText("Nama Penerima")
        self.namaPenerima.setFixedSize(320, 46)
        self.namaPenerima.move(773, 279)
        self.namaPenerima.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.namaPenerima.textChanged.connect(self.setNamaPenerima)
        
        # set nama instansi
        self.namaInstansi = QTextEdit(self)
        self.namaInstansi.setPlaceholderText("Nama Instansi")
        self.namaInstansi.setFixedSize(320, 46)
        self.namaInstansi.move(773, 339)
        self.namaInstansi.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.namaInstansi.textChanged.connect(self.setNamaInstansi)
        
        # set upload RM
        self.targetDonasi = QTextEdit(self)
        self.targetDonasi.setPlaceholderText("Target Donasi (Rp)")
        self.targetDonasi.setFixedSize(320, 46)
        self.targetDonasi.move(773, 409)
        self.targetDonasi.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.targetDonasi.textChanged.connect(self.setTargetDonasi)

        # LOWER
        self.deskripsi = QTextEdit(self)
        self.deskripsi.setPlaceholderText("Deskripsi")
        self.deskripsi.setFixedSize(757, 116)
        self.deskripsi.move(336, 479)
        self.deskripsi.textChanged.connect(self.setDeskripsi)
        
        # set submit button
        self.submitFormNK = QPushButton(self)
        self.submitFormNK.setText("SUBMIT")
        self.submitFormNK.setFixedSize(165, 52)
        self.submitFormNK.move(638, 634)
        self.submitFormNK.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.submitFormNK.clicked.connect(self.goToRiwayatPenggalangan)

        self.returnButton = QPushButton(self)
        self.returnButton.setText("< Kembali ke Laman Utama")
        self.returnButton.setFixedSize(258, 36)
        self.returnButton.move(53, 32)
        self.returnButton.clicked.connect(self.goToHome)

    def goToHome(self):
        self.channel.emit()

    def resetState(self):
        self.judul.clear()
        self.namaPenerima.clear()
        self.namaInstansi.clear()
        self.deskripsi.clear()
        self.fb.clear()
        self.ig.clear()
        self.twitter.clear()
        self.targetDonasi.clear()
        self.deskripsi.clear()
        for key in list(self.dataText.keys()):
            self.dataText[key] = ""

    def setJudul(self):
        self.dataText["judul"] = self.judul.toPlainText()

    def setDeskripsi(self):
        self.dataText["deskripsi"] = self.deskripsi.toPlainText()
    
    def setTargetDonasi(self):
        self.dataText["target"] = self.targetDonasi.toPlainText()
        
    def setNamaInstansi(self):
        self.dataText["instansi"] = self.namaInstansi.toPlainText()
        
    def setIg(self):
        self.dataText["akun-instagram"] = self.ig.toPlainText()
    
    def setTwitter(self):
        self.dataText["akun-twitter"] = self.twitter.toPlainText()
    
    def setFb(self):
        self.dataText["akun-facebook"] = self.fb.toPlainText()
    
    def setNamaPenerima(self):
        self.dataText["nama-penerima"] = self.namaPenerima.toPlainText()
    
        
    def sendData(self):
        response = requests.post('http://localhost:3000/permintaan/create-permintaan-lainnya', data=self.dataText,
            auth=HTTPBasicAuth(self.session["username-email"], self.session["password"])
        )
        if (response.status_code == 201):
            return True
        else:
            return False
    
    def goToRiwayatPenggalangan(self):
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


# if(__name__ == "__main__"):
#     app = QApplication(sys.argv)
#     window = FormNonKesehatan()
#     window.show()
#     sys.exit(app.exec())