from PyQt6.QtWidgets import QLabel, QTextEdit, QPushButton, QWidget, QFileDialog, QMessageBox
from PyQt6.QtGui import QCursor
from PyQt6.QtCore import Qt, pyqtSignal
from requests.auth import HTTPBasicAuth
import requests

class FormKesehatan(QWidget):
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
        "tujuan": "",
        "nama-pasien": ""
    }

    dataFile = {
        "foto-ktp": "",
        "foto-kk": "",
        "foto-ket-medis": "",
        "foto-pemeriksaan": "",
    }

    def __init__(self):
        super().__init__()
        
        # set overall page layout
        self.setFixedSize(1440, 1024)
        self.setWindowTitle("KITASABI - Form Penggalangan Dana Kesehatan")
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
        # set title label
        self.text = QLabel(self)
        self.text.setText("Form Penggalangan Dana Kesehatan")
        self.text.move(401, 88)

        # LEFTSIDE5A4FF3
        # set judul
        self.judul = QTextEdit(self)
        self.judul.setPlaceholderText("Judul")
        self.judul.setFixedSize(320, 46)
        self.judul.move(336, 219)
        self.judul.textChanged.connect(self.setJudul)

        # set nama
        self.nama = QTextEdit(self)
        self.nama.setPlaceholderText("Nama")
        self.nama.setFixedSize(320, 46)
        self.nama.move(336, 289)
        self.nama.textChanged.connect(self.setNama)

        # set penyakit yang diderita
        self.penyakit = QTextEdit(self)
        self.penyakit.setPlaceholderText("Penyakit yang Diderita")
        self.penyakit.setFixedSize(320, 46)
        self.penyakit.move(336, 349)
        self.penyakit.textChanged.connect(self.setPenyakit)

        # set tujuan
        self.tujuan = QTextEdit(self)
        self.tujuan.setPlaceholderText("Tujuan")
        self.tujuan.setFixedSize(320, 41)
        self.tujuan.move(336, 429)
        self.tujuan.textChanged.connect(self.setTujuan)

        # RIGHTSIDE
        # set upload KTP
        self.uploadKTP = QPushButton(self)
        self.uploadKTP.setText("KTP Penggalang Dana")
        self.uploadKTP.setFixedSize(320, 46)
        self.uploadKTP.move(773, 219)
        self.uploadKTP.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.uploadKTP.clicked.connect(self.openKTP)

        # set upload KK
        self.uploadKK = QPushButton(self)
        self.uploadKK.setText("Kartu Keluarga")
        self.uploadKK.setFixedSize(320, 46)
        self.uploadKK.move(773, 289)
        self.uploadKK.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.uploadKK.clicked.connect(self.openKK)

        # set upload SKM
        self.uploadSKM = QPushButton(self)
        self.uploadSKM.setText("Surat Keterangan Medis")
        self.uploadSKM.setFixedSize(320, 46)
        self.uploadSKM.move(773, 349)
        self.uploadSKM.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.uploadSKM.clicked.connect(self.openSKM)

        # set upload HP
        self.uploadHP = QPushButton(self)
        self.uploadHP.setText("Hasil Pemeriksaan")
        self.uploadHP.setFixedSize(320, 46)
        self.uploadHP.move(773, 429)
        self.uploadHP.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.uploadHP.clicked.connect(self.openHP)

        # LOWER
        self.deskripsi = QTextEdit(self)
        self.deskripsi.setPlaceholderText("Deskripsi")
        self.deskripsi.setFixedSize(757, 96)
        self.deskripsi.move(336, 499)
        self.deskripsi.textChanged.connect(self.setDeskripsi)

        self.target = QTextEdit(self)
        self.target.setPlaceholderText("Target Donasi (Rp)")
        self.target.setFixedSize(317, 46)
        self.target.move(556, 619)
        self.target.textChanged.connect(self.setTarget)

        # set submit button
        self.submitFormK = QPushButton(self)
        self.submitFormK.setText("SUBMIT")
        self.submitFormK.setFixedSize(165, 52)
        self.submitFormK.move(638, 684)
        self.submitFormK.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.submitFormK.clicked.connect(self.goToRiwayatPenggalangan)

    def resetState(self):
        self.judul.clear()
        self.nama.clear()
        self.penyakit.clear()
        self.tujuan.clear()
        self.deskripsi.clear()
        self.target.clear()
        for key in list(self.dataText.keys()):
            self.dataText[key] = ""
        for key in list(self.dataFile.keys()):
            self.dataFile[key] = ""

    def setJudul(self):
        self.dataText["judul"] = self.judul.toPlainText()
    def setNama(self):
        self.dataText["nama"] = self.nama.toPlainText()
    def setPenyakit(self):
        self.dataText["penyakit"] = self.penyakit.toPlainText()
    def setTujuan(self):
        self.dataText["tujuan"] = self.tujuan.toPlainText()
    def setDeskripsi(self):
        self.dataText["deskripsi"] = self.deskripsi.toPlainText()
    def setTarget(self):
        self.dataText["target"] = self.target.toPlainText()

    def sendData(self):
        response = requests.post('http://localhost:3000/permintaan/create-permintaan-kesehatan', data=self.dataText, files=self.dataFile,
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
            
    def openKTP(self):
        self.openFile("foto-ktp")

    def openKK(self):
        self.openFile("foto-kk")

    def openSKM(self):
        self.openFile("foto-ket-medis")
    
    def openHP(self):
        self.openFile("foto-pemeriksaan")
    
    def openFile(self, type):
        file = QFileDialog.getOpenFileName(self, 'Open a file', '', 'Image(*.jpg);;PDF(*.pdf);;Word(*.docx)')
        if file != ('', ''):
            path = file[0]
            self.dataFile[type] = open(path, "rb")
                
            