from PyQt6.QtWidgets import QApplication, QLabel, QTextEdit, QPushButton, QWidget
from PyQt6.QtGui import QCursor
from PyQt6.QtCore import Qt, pyqtSignal
import sys

class FormNonKesehatan(QWidget):
    channel = pyqtSignal()
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

        # set nama
        self.nama = QTextEdit(self)
        self.nama.setPlaceholderText("Nama")
        self.nama.setFixedSize(320, 46)
        self.nama.move(336, 249)
        self.nama.setStyleSheet('''
            border: 2px solid #5A4FF3;
            background-color: #FFFFFF;
            padding: 10px 10px 10px 10px;
        ''')

        # set pekerjaan
        self.pekerjaan = QTextEdit(self)
        self.pekerjaan.setPlaceholderText("Pekerjaan")
        self.pekerjaan.setFixedSize(320, 46)
        self.pekerjaan.move(336, 319)
        self.pekerjaan.setStyleSheet('''
            border: 2px solid #5A4FF3;
            background-color: #FFFFFF;
            padding: 10px 10px 10px 10px;
        ''')

        # set tujuan
        self.tujuan = QTextEdit(self)
        self.tujuan.setPlaceholderText("Tujuan")
        self.tujuan.setFixedSize(320, 116)
        self.tujuan.move(336, 389)
        self.tujuan.setStyleSheet('''
            border: 2px solid #5A4FF3;
            background-color: #FFFFFF;
            padding: 10px 10px 10px 10px;
        ''')

        # RIGHTSIDE
        # set no telepon
        self.noTelp = QPushButton(self)
        self.noTelp.setText("No Telepon")
        self.noTelp.setFixedSize(320, 46)
        self.noTelp.move(773, 179)
        self.noTelp.setStyleSheet('''
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
        self.noTelp.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        # set nama penerima
        self.namaPenerima = QPushButton(self)
        self.namaPenerima.setText("Nama Penerima")
        self.namaPenerima.setFixedSize(320, 46)
        self.namaPenerima.move(773, 249)
        self.namaPenerima.setStyleSheet('''
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
        self.namaPenerima.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        # set nama instansi
        self.namaInstansi = QPushButton(self)
        self.namaInstansi.setText("Nama Instansi")
        self.namaInstansi.setFixedSize(320, 46)
        self.namaInstansi.move(773, 319)
        self.namaInstansi.setStyleSheet('''
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
        self.namaInstansi.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        # set akun medsos
        self.akunMedsos = QPushButton(self)
        self.akunMedsos.setText("Akun Media Sosial")
        self.akunMedsos.setFixedSize(320, 46)
        self.akunMedsos.move(773, 389)
        self.akunMedsos.setStyleSheet('''
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
        self.akunMedsos.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        # set upload RM
        self.targetDonasi = QPushButton(self)
        self.targetDonasi.setText("Target Donasi (Rp)")
        self.targetDonasi.setFixedSize(320, 46)
        self.targetDonasi.move(773, 459)
        self.targetDonasi.setStyleSheet('''
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
        self.targetDonasi.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

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

    def goToRiwayatPenggalangan(self):
        self.channel.emit()


# app = QApplication(sys.argv)
# window = FormNonKesehatan()
# window.show()
# sys.exit(app.exec())