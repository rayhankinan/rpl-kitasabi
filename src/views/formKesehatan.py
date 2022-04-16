from PyQt6.QtWidgets import QLabel, QTextEdit, QPushButton, QDialog, QFileDialog
from PyQt6.QtGui import QCursor
from PyQt6.QtCore import Qt

class FormKesehatan(QDialog):
    def __init__(self, value):
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

        # set upload RM
        self.uploadRM = QPushButton(self)
        self.uploadRM.setText("Riwayat Medis")
        self.uploadRM.setFixedSize(320, 46)
        self.uploadRM.move(773, 429)
        self.uploadRM.setStyleSheet('''
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
        self.uploadRM.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.uploadRM.clicked.connect(self.openRM)

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

        self.target = QTextEdit(self)
        self.target.setPlaceholderText("Target Donasi (Rp)")
        self.target.setFixedSize(317, 46)
        self.target.move(556, 619)
        self.target.setStyleSheet('''
            border: 2px solid #5A4FF3;
            background-color: #FFFFFF;
            padding: 10px 10px 10px 10px;
        ''')

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
        # self.submitFormK.clicked.connect(send)

    def openKTP(self):
        self.openFile("KTP")

    def openKK(self):
        self.openFile("KK")

    def openSKM(self):
        self.openFile("SKM")
    
    def openHP(self):
        self.openFile("HP")
    
    def openRM(self):
        self.openFile("RM")

    def openFile(self, type):
        if (type == "KTP"):
            print("KTP")
        elif (type == "KK"):
            print("KK")
        elif (type == "SKM"):
            print("SKM")
        elif (type == "HP"):
            print("HP")
        else:
            print("RM")
        file = QFileDialog.getOpenFileName(self, 'Open a file', '', 'Image(*.jpg);;PDF(*.pdf);;Word(*.docx)')
        if file != ('', ''):
            path = file[0]
            print(path)
            # TEST OPEN TXT FILE
            # with open(path, "r") as f:
            #     print(f.readline())
            