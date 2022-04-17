import sys
from PyQt6.QtWidgets import QApplication, QWidget, QTextEdit, QLabel, QLineEdit, QPushButton, QMessageBox
from PyQt6.QtGui import QFont, QPixmap, QCursor, QImage
from PyQt6.QtCore import Qt
from PyQt6.QtCore import pyqtSignal
from custom_widgets import ClickableLabel
import urllib.request

import sys
import urllib.request

graybg = '#F2F4F7'
ungu = 'rgba(90, 79, 243, 1)'
white = 'rgba(255, 255, 255, 1)'
tulisan = 'rgba(37, 49, 60, 1)'

class RiwayatDonasiWindow(QWidget):
  switch = pyqtSignal(str, dict)

  def __init__(self):
    super().__init__()
    self.setUpRiwayatDonasiWindow()
    
  def setUpRiwayatDonasiWindow(self):
    self.setFixedSize(1440, 1024)
    self.setWindowTitle("KITASABI - Laman Riwayat Donasi")
    self.setUpWidgets()
    
  def setUpWidgets(self):
    # Set warna background
    self.setStyleSheet('background-color: #E5E5E5')
    
    # set up font
    mulish16 = QFont()
    mulish16.setFamily("Mulish"); mulish16.setPixelSize(16)
    
    mulish24 = QFont()
    mulish24.setFamily("Mulish"); mulish24.setPixelSize(24)
    
    mulish24_bold = QFont()
    mulish24_bold.setFamily("Mulish"); mulish24.setPixelSize(24)
    mulish24_bold.setBold(True)
    
    mulish33_bold = QFont()
    mulish33_bold.setFamily("Mulish"); mulish33_bold.setPixelSize(33)
    mulish33_bold.setBold(True)
        
    mulish44 = QFont()
    mulish44.setFamily("Mulish"); mulish44.setPixelSize(44)
    mulish44.setBold(True)
    
    # return button
    self.returnButton = QPushButton(self)
    self.returnButton.setText("< Kembali ke Laman Eksplor")
    self.returnButton.setFixedSize(282, 56)
    self.returnButton.move(47, 49)
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
    
    # label riwayat penggalangan dana
    self.labelRiwayatPenggalanganDana = QLabel(self)
    self.labelRiwayatPenggalanganDana.setText("Riwayat Penggalangan Dana")
    # align center text
    self.labelRiwayatPenggalanganDana.setAlignment(Qt.AlignmentFlag.AlignCenter)
    self.labelRiwayatPenggalanganDana.setFont(mulish33_bold)
    self.labelRiwayatPenggalanganDana.setFixedSize(768,73)
    self.labelRiwayatPenggalanganDana.setStyleSheet('background-color: rgba(187, 200, 212, 1)')
    self.labelRiwayatPenggalanganDana.move(355, 172)

    # Mulai Penggalangan Dana Button
    # tombol mulai penggalangan dana
    self.mulai_penggalangan_button = QPushButton(self)
    self.mulai_penggalangan_button.setText("Mulai Penggalangan Dana")
    self.labelRiwayatPenggalanganDana.setAlignment(Qt.AlignmentFlag.AlignCenter)
    self.mulai_penggalangan_button.setFixedSize(321, 56)
    self.mulai_penggalangan_button.move(602,289)
    self.mulai_penggalangan_button.setStyleSheet('''
      QPushButton {
        color: #ffffff;
        background-color: #3643fc;
        border: none;
        border-radius: 12px;
      }
      QPushButton:hover {
        background-color: #6b75ff;
      }
    ''')
    self.mulai_penggalangan_button.setFont(mulish24)
    self.mulai_penggalangan_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
    # self.mulai_penggalangan_button.clicked.connect(self.showPenggalanganDanaWindow)
    
    
    
    # set background
    self.cardBackground = QLabel(self)
    self.cardBackground.setFixedSize(1220, 546)
    self.cardBackground.move(124, 440)
    self.cardBackground.setStyleSheet('background-color: rgba(187, 200, 212, 1)')
    
    # set preview penggalangan dana
    bg_list = QLabel(self)
    bg_list.setFixedSize(956, 144)
    bg_list.setStyleSheet(f'background-color: {graybg}')
    bg_list.move(271,474)
    # Preview penggalangan dana +i *185
    self.judul_penggalangan_dana = QLabel(self)
    self.judul_penggalangan_dana.setText("Judul Penggalangan Dana")
    self.judul_penggalangan_dana.setStyleSheet('color: rgba(37, 49, 60, 1)')
    self.judul_penggalangan_dana.setStyleSheet('background-color: #F2F4F7')
    self.judul_penggalangan_dana.move(443, 505) 
    self.judul_penggalangan_dana.setFont(mulish24)
    # nominal penggalangan dana
    self.nominal = QLabel(self)
    self.nominal.setText("Nominal")
    self.nominal.setStyleSheet('color: rgba(37, 49, 60, 1)')
    self.nominal.setStyleSheet('background-color: #F2F4F7')
    self.nominal.move(443, 549)
    self.nominal.setFont(mulish24)
    # foto          
    url2 = 'https://yt3.ggpht.com/ytc/AKedOLQU2qqsQIYjE4SgWbHOYL4QkPO6dEXBcV8SnYEDig=s900-c-k-c0x00ffffff-no-rj'
    data2 = urllib.request.urlopen(url2).read()
    image2 = QImage()
    image2.loadFromData(data2)
    self.previewImg2 = QLabel(self)
    self.previewImg2.setFixedSize(117, 117)
    self.previewImg2.move(287, 487)
    self.previewImg2.setScaledContents(True)
    pixmap2 = QPixmap(image2)
    self.previewImg2.setPixmap(pixmap2)
    # cairkan button
    self.cairkan_button = QPushButton(self)
    self.cairkan_button.setText("Cairkan")
    self.cairkan_button.setFixedSize(165, 56)
    self.cairkan_button.move(990, 518)
    self.cairkan_button.setFont(mulish24)
    self.cairkan_button.setStyleSheet('''
        QPushButton {
          color: #ffffff;
          background-color: #3643fc;
          border: none;
          border-radius: 12px;
        }
        QPushButton:hover {
          background-color: #6b75ff;
        }
    ''')
    self.cairkan_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
    
    
    
if __name__ == "__main__":
  app = QApplication(sys.argv)
  window = RiwayatDonasiWindow()
  window.show()
  sys.exit(app.exec())