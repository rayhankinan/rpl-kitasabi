from PyQt6.QtWidgets import QLabel, QTextEdit, QPushButton, QWidget, QFileDialog
from PyQt6.QtGui import QCursor
from PyQt6.QtCore import Qt, pyqtSignal
import base64
import requests


class FormKesehatan(QWidget):
    channel = pyqtSignal()
    
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
        # set title label
        self.text = QLabel(self)
        self.text.setText("Form Penggalangan Dana Kesehatan")
        self.text.setStyleSheet('''
            color: #25313C;
            font-weight: bold;
            font-size: 38px;
        ''')
        self.text.move(401, 53)

        # LEFTSIDE
        # set judul
        self.judul = QTextEdit(self)
        self.judul.setPlaceholderText("Judul")
        self.judul.setFixedSize(320, 46)
        self.judul.move(336, 149)
        self.judul.setStyleSheet('''
            border: 2px solid #5A4FF3;
            background-color: #FFFFFF;
            padding: 10px 10px 10px 10px;
        ''')
        self.judul.textChanged.connect(self.setJudul)

        # set nama
        self.nama = QTextEdit(self)
        self.nama.setPlaceholderText("Nama")
        self.nama.setFixedSize(320, 46)
        self.nama.move(336, 219)
        self.nama.setStyleSheet('''
            border: 2px solid #5A4FF3;
            background-color: #FFFFFF;
            padding: 10px 10px 10px 10px;
        ''')
        self.nama.textChanged.connect(self.setNama)

        # set penyakit yang diderita
        self.penyakit = QTextEdit(self)
        self.penyakit.setPlaceholderText("Penyakit yang Diderita")
        self.penyakit.setFixedSize(320, 46)
        self.penyakit.move(336, 289)
        self.penyakit.setStyleSheet('''
            border: 2px solid #5A4FF3;
            background-color: #FFFFFF;
            padding: 10px 10px 10px 10px;
        ''')
        self.penyakit.textChanged.connect(self.setPenyakit)

        # set tujuan
        self.tujuan = QTextEdit(self)
        self.tujuan.setPlaceholderText("Tujuan")
        self.tujuan.setFixedSize(320, 116)
        self.tujuan.move(336, 359)
        self.tujuan.setStyleSheet('''
            border: 2px solid #5A4FF3;
            background-color: #FFFFFF;
            padding: 10px 10px 10px 10px;
        ''')
        self.tujuan.textChanged.connect(self.setTujuan)

        # RIGHTSIDE
        # set upload KTP
        self.uploadKTP = QPushButton(self)
        self.uploadKTP.setText("KTP Penggalang Dana")
        self.uploadKTP.setFixedSize(320, 46)
        self.uploadKTP.move(773, 149)
        self.uploadKTP.setStyleSheet('''
            QPushButton {
                border: 2px solid #5A4FF3;
                background-color: #FFFFFF;
                padding: 10px 10px 10px 10px;
            }
            QPushButton:hover {
                background-color: #5A4FF3;
                color: white;
            }
        ''')
        self.uploadKTP.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.uploadKTP.clicked.connect(self.openKTP)

        # set upload KK
        self.uploadKK = QPushButton(self)
        self.uploadKK.setText("Kartu Keluarga")
        self.uploadKK.setFixedSize(320, 46)
        self.uploadKK.move(773, 219)
        self.uploadKK.setStyleSheet('''
            QPushButton {
                border: 2px solid #5A4FF3;
                background-color: #FFFFFF;
                padding: 10px 10px 10px 10px;
            }
            QPushButton:hover {
                background-color: #5A4FF3;
                color: white;
            }
        ''')
        self.uploadKK.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.uploadKK.clicked.connect(self.openKK)

        # set upload SKM
        self.uploadSKM = QPushButton(self)
        self.uploadSKM.setText("Surat Keterangan Medis")
        self.uploadSKM.setFixedSize(320, 46)
        self.uploadSKM.move(773, 289)
        self.uploadSKM.setStyleSheet('''
            QPushButton {
                border: 2px solid #5A4FF3;
                background-color: #FFFFFF;
                padding: 10px 10px 10px 10px;
            }
            QPushButton:hover {
                background-color: #5A4FF3;
                color: white;
            }
        ''')
        self.uploadSKM.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.uploadSKM.clicked.connect(self.openSKM)

        # set upload HP
        self.uploadHP = QPushButton(self)
        self.uploadHP.setText("Hasil Pemeriksaan")
        self.uploadHP.setFixedSize(320, 46)
        self.uploadHP.move(773, 359)
        self.uploadHP.setStyleSheet('''
            QPushButton {
                border: 2px solid #5A4FF3;
                background-color: #FFFFFF;
                padding: 10px 10px 10px 10px;
            }
            QPushButton:hover {
                background-color: #5A4FF3;
                color: white;
            }
        ''')
        self.uploadHP.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.uploadHP.clicked.connect(self.openHP)

        # # set upload RM
        # self.uploadRM = QPushButton(self)
        # self.uploadRM.setText("Riwayat Medis")
        # self.uploadRM.setFixedSize(320, 46)
        # self.uploadRM.move(773, 429)
        # self.uploadRM.setStyleSheet('''
        #     QPushButton {
        #         border: 2px solid #5A4FF3;
        #         background-color: #FFFFFF;
        #         padding: 10px 10px 10px 10px;
        #     }
        #     QPushButton:hover {
        #         background-color: #5A4FF3;
        #         color: white;
        #     }
        # ''')
        # self.uploadRM.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        # self.uploadRM.clicked.connect(self.openRM)

        # LOWER
        self.deskripsi = QTextEdit(self)
        self.deskripsi.setPlaceholderText("Deskripsi")
        self.deskripsi.setFixedSize(757, 96)
        self.deskripsi.move(336, 499)
        self.deskripsi.setStyleSheet('''
            border: 2px solid #5A4FF3;
            background-color: #FFFFFF;
            padding: 10px 10px 10px 10px;
        ''')
        self.deskripsi.textChanged.connect(self.setDeskripsi)

        self.target = QTextEdit(self)
        self.target.setPlaceholderText("Target Donasi (Rp)")
        self.target.setFixedSize(317, 46)
        self.target.move(556, 619)
        self.target.setStyleSheet('''
            border: 2px solid #5A4FF3;
            background-color: #FFFFFF;
            padding: 10px 10px 10px 10px;
        ''')
        self.target.textChanged.connect(self.setTarget)

        # set submit button
        self.submitFormK = QPushButton(self)
        self.submitFormK.setText("SUBMIT")
        self.submitFormK.setFixedSize(165, 52)
        self.submitFormK.move(638, 684)
        self.submitFormK.setStyleSheet('''
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
        self.submitFormK.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.submitFormK.clicked.connect(self.goToRiwayatPenggalangan)

    def resetState(self):
        self.judul.clear()
        self.nama.clear()
        self.penyakit.clear()
        self.tujuan.clear()
        self.deskripsi.clear()
        self.target.clear()

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
        response = requests.post('http://localhost:3000/permintaan/create-permintaan-kesehatan', data=self.dataText, files=self.dataFile)
        if (response.status_code == 201):
            print("BERHASIL")
        else:
            print("GAGAL")

    def goToRiwayatPenggalangan(self):
        self.sendData()
        self.resetState()
        self.channel.emit()

    def openKTP(self):
        self.openFile("foto-ktp")

    def openKK(self):
        self.openFile("foto-kk")

    def openSKM(self):
        self.openFile("foto-ket-medis")
    
    def openHP(self):
        self.openFile("foto-pemeriksaan")
    
    # def openRM(self):
    #     self.openFile("foto-riwayat-medis")

    def openFile(self, type):
        file = QFileDialog.getOpenFileName(self, 'Open a file', '', 'Image(*.jpg);;PDF(*.pdf);;Word(*.docx)')
        if file != ('', ''):
            path = file[0]
            print(path)
            # TEST OPEN TXT FILE
            self.dataFile[type] = open(path, "rb")
                
            