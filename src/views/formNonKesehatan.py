from urllib import response
from PyQt6.QtWidgets import QApplication, QLabel, QPushButton, QTextEdit, QWidget
from PyQt6.QtGui import QCursor
from PyQt6.QtCore import Qt, pyqtSignal
import requests
import sys

class FormNonKesehatan(QWidget):
    channel = pyqtSignal()
    
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
        self.text = QLabel(self)
        self.text.setText("Form Non-Kesehatan")
        self.text.setStyleSheet('''
            color: #25313C;
            font-weight: bold;
            font-size: 38px;
        ''')
        self.text.move(561, 53)

        # LEFTSIDE
        # set judul
        self.judul = QTextEdit(self)
        self.judul.setPlaceholderText("Judul")
        self.judul.setFixedSize(320, 46)
        self.judul.move(336, 179)
        self.judul.setStyleSheet('''
            border: 2px solid #5A4FF3;
            background-color: #FFFFFF;
            padding: 10px 10px 10px 10px;
        ''')
        self.judul.textChanged.connect(self.setJudul)

        # set nama
        self.namaPenerima = QTextEdit(self)
        self.namaPenerima.setPlaceholderText("Nama Penerima")
        self.namaPenerima.setFixedSize(320, 46)
        self.namaPenerima.move(336, 249)
        self.namaPenerima.setStyleSheet('''
            border: 2px solid #5A4FF3;
            background-color: #FFFFFF;
            padding: 10px 10px 10px 10px;
        ''')
        self.namaPenerima.textChanged.connect(self.setNamaPenerima)

        # set fb
        self.fb = QTextEdit(self)
        self.fb.setPlaceholderText("facebook")
        self.fb.setFixedSize(320, 46)
        self.fb.move(336, 319)
        self.fb.setStyleSheet('''
            border: 2px solid #5A4FF3;
            background-color: #FFFFFF;
            padding: 10px 10px 10px 10px;
        ''')
        self.fb.textChanged.connect(self.setFb)


        # set ig
        self.ig = QTextEdit(self)
        self.ig.setPlaceholderText("instagram")
        self.ig.setFixedSize(320, 116)
        self.ig.move(336, 389)
        self.ig.setStyleSheet('''
            border: 2px solid #5A4FF3;
            background-color: #FFFFFF;
            padding: 10px 10px 10px 10px;
        ''')
        self.ig.textChanged.connect(self.setIg)

        # RIGHTSIDE
        # set twitter
        self.twitter = QTextEdit(self)
        self.twitter.setPlaceholderText("Twitter")
        self.twitter.setFixedSize(320, 46)
        self.twitter.move(773, 179)
        self.twitter.setStyleSheet('''
            border: 2px solid #5A4FF3;
            background-color: #FFFFFF;
            padding: 10px 10px 10px 10px;
        ''')
        self.twitter.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.twitter.textChanged.connect(self.setTwitter)
        
        # set nama penerima
        self.namaPenerima = QTextEdit(self)
        self.namaPenerima.setPlaceholderText("Nama Penerima")
        self.namaPenerima.setFixedSize(320, 46)
        self.namaPenerima.move(773, 249)
        self.namaPenerima.setStyleSheet('''
            border: 2px solid #5A4FF3;
            background-color: #FFFFFF;
            padding: 10px 10px 10px 10px;
        ''')
        self.namaPenerima.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.namaPenerima.textChanged.connect(self.setNamaPenerima)
        
        # set nama instansi
        self.namaInstansi = QTextEdit(self)
        self.namaInstansi.setPlaceholderText("Nama Instansi")
        self.namaInstansi.setFixedSize(320, 46)
        self.namaInstansi.move(773, 319)
        self.namaInstansi.setStyleSheet('''
            border: 2px solid #5A4FF3;
            background-color: #FFFFFF;
            padding: 10px 10px 10px 10px;
        ''')
        self.namaInstansi.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.namaInstansi.textChanged.connect(self.setNamaInstansi)

        
        # set upload RM
        self.targetDonasi = QTextEdit(self)
        self.targetDonasi.setPlaceholderText("Target Donasi (Rp)")
        self.targetDonasi.setFixedSize(320, 46)
        self.targetDonasi.move(773, 459)
        self.targetDonasi.setStyleSheet('''
            border: 2px solid #5A4FF3;
            background-color: #FFFFFF;
            padding: 10px 10px 10px 10px;
        ''')
        self.targetDonasi.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.targetDonasi.textChanged.connect(self.setTargetDonasi)

        # LOWER
        self.deskripsi = QTextEdit(self)
        self.deskripsi.setPlaceholderText("Deskripsi")
        self.deskripsi.setFixedSize(757, 116)
        self.deskripsi.move(336, 529)
        self.deskripsi.setStyleSheet('''
            border: 2px solid #5A4FF3;
            background-color: #FFFFFF;
            padding: 10px 10px 10px 10px;
        ''')
        self.deskripsi.textChanged.connect(self.setDeskripsi)
        
        # set submit button
        self.submitFormNK = QPushButton(self)
        self.submitFormNK.setText("SUBMIT")
        self.submitFormNK.setFixedSize(165, 52)
        self.submitFormNK.move(638, 684)
        self.submitFormNK.setStyleSheet('''
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
                color: black;
            }
        ''')
        self.submitFormNK.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.submitFormNK.clicked.connect(self.goToRiwayatPenggalangan)

    def resetState(self):
        self.judul.clear()
        self.nama.clear()
        self.instansi.clear()
        self.tujuan.clear()
        self.noTelp.clear()
        self.namaPenerima.clear()
        self.namaInstansi.clear()
        self.akunMedsos.clear()
        self.targetDonasi.clear()
        self.deskripsi.clear()

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
        response = requests.post('http://localhost:3000/permintaan/create-permintaan-lainnya', data=self.dataText)
        if (response.status_code == 201):
            print("BERHASIL")
        else:
            print("GAGAL")
    
    def goToRiwayatPenggalangan(self):
        self.sendData()
        self.resetState()
        self.channel.emit()


if(__name__ == "__main__"):
    app = QApplication(sys.argv)
    window = FormNonKesehatan()
    window.show()
    sys.exit(app.exec())