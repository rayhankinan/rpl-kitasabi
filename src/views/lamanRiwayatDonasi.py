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
  channel = pyqtSignal()

  def __init__(self):
    super().__init__()
    self.pageRiwayatDonasi = 0
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
    self.initializeRiwayatDonasi()
    self.setUpDisplayRiwayatDonasi()
    self.returnButton.clicked.connect(self.goToLamanEksplor)
    
    # next button
    nextButton = QPushButton(self)
    nextButton.setText(">")
    nextButton.setFixedSize(40, 71)
    nextButton.move(1336,426)
    nextButton.setStyleSheet('''
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
    nextButton.setFont(mulish44)
    nextButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
    # nextButton.clicked.connect(self.nextRiwayatDonasi())
    
    # previous button
    previousButton = QPushButton(self)
    previousButton.setText("<")
    previousButton.setFixedSize(40, 71)
    previousButton.move(76,426)
    previousButton.setStyleSheet('''
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
    previousButton.setFont(mulish44)
    previousButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
    # previousButton.clicked.connect(self.previousRiwayatDonasi())
      
    # label riwayat donasi
    
  def initializeRiwayatDonasi(self):
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
    
    
    self.labelRiwayatDonasi = QLabel(self)
    self.labelRiwayatDonasi.setText("Riwayat Donasi")
    # align center text
    self.labelRiwayatDonasi.setAlignment(Qt.AlignmentFlag.AlignCenter)
    self.labelRiwayatDonasi.setFont(mulish33_bold)
    self.labelRiwayatDonasi.setFixedSize(433,37)
    self.labelRiwayatDonasi.setStyleSheet('background-color: rgba(187, 200, 212, 1)')
    self.labelRiwayatDonasi.move(452, 96)

    # set background
    self.cardBackground = QLabel(self)
    self.cardBackground.setFixedSize(1220, 608)
    self.cardBackground.move(116, 158)
    self.cardBackground.setStyleSheet('background-color: rgba(187, 200, 212, 1)')
    
    self.riwayatDonasiCard = []
    for i in range(3):
      self.riwayatDonasiCard.append({})
      # set preview penggalangan dana
      self.riwayatDonasiCard[i]["bg_list"] = QLabel(self)
      self.riwayatDonasiCard[i]["bg_list"].setFixedSize(956, 158)
      self.riwayatDonasiCard[i]["bg_list"].setStyleSheet(f'background-color: {graybg}')
      self.riwayatDonasiCard[i]["bg_list"].move(253,199+i *185)
        # Preview penggalangan dana +i *185
      self.riwayatDonasiCard[i]["preview_penggalangan_dana"] = QLabel(self)
      self.riwayatDonasiCard[i]["preview_penggalangan_dana"].setText("Judul Penggalangan Dana")
      self.riwayatDonasiCard[i]["preview_penggalangan_dana"].setStyleSheet('color: rgba(37, 49, 60, 1)')
      self.riwayatDonasiCard[i]["preview_penggalangan_dana"].setStyleSheet('background-color: #F2F4F7')
      self.riwayatDonasiCard[i]["preview_penggalangan_dana"].move(425, 233 +i*185) 
      self.riwayatDonasiCard[i]["preview_penggalangan_dana"].setFont(mulish24)
      # nominal penggalangan dana
      self.riwayatDonasiCard[i]["nominal"] = QLabel(self)
      self.riwayatDonasiCard[i]["nominal"].setText("Nominal")
      self.riwayatDonasiCard[i]["nominal"].setStyleSheet('color: rgba(37, 49, 60, 1)')
      self.riwayatDonasiCard[i]["nominal"].setStyleSheet('background-color: #F2F4F7')
      self.riwayatDonasiCard[i]["nominal"].move(425, 282 +i*185)
      self.riwayatDonasiCard[i]["nominal"].setFont(mulish24)
      # foto          
      self.url2 = 'https://yt3.ggpht.com/ytc/AKedOLQU2qqsQIYjE4SgWbHOYL4QkPO6dEXBcV8SnYEDig=s900-c-k-c0x00ffffff-no-rj'
      self.data2 = urllib.request.urlopen(self.url2).read()
      self.image2 = QImage()
      self.image2.loadFromData(self.data2)
      self.riwayatDonasiCard[i]["previewImg2"] = QLabel(self)
      self.riwayatDonasiCard[i]["previewImg2"].setFixedSize(117, 128)
      self.riwayatDonasiCard[i]["previewImg2"].move(269, 213 +i*185)
      self.riwayatDonasiCard[i]["previewImg2"].setScaledContents(True)
      self.pixmap2 = QPixmap(self.image2)
      self.riwayatDonasiCard[i]["previewImg2"].setPixmap(self.pixmap2)

  def setUpDisplayRiwayatDonasi(self):
    start = self.pageRiwayatDonasi * 3
    # for i in range(3):
    #   # if start + i < len(self.databaseRiwayatDonasi):
    #     # Preview penggalangan dana +i *185
    #     self.riwayatDonasiCard[i]["preview_penggalangan_dana"].setText("Judul Penggalangan Dana")
    #     # nominal penggalangan dana
    #     self.riwayatDonasiCard[i]["nominal"].setText("Nominal")
    #     # foto          
    #     self.url2 = 'https://yt3.ggpht.com/ytc/AKedOLQU2qqsQIYjE4SgWbHOYL4QkPO6dEXBcV8SnYEDig=s900-c-k-c0x00ffffff-no-rj'   
      
  
  def nextRiwayatDonasi(self):
    print("Right button clicked")
    # if (self.pageRiwayatDonasi + 1 < (len(self.databaseRiwayatDonasi)//3)):
    #     self.pageRiwayatDonasi += 1
    #     print("page: ", self.pageRiwayatDonasi)
    #     self.setUpDisplayRiwayatDonasi()
    # else:
    #     print("No more RiwayatDonasi")

  def previousRiwayatDonasi(self):
    print("Left button clicked")
    # if (self.pageRiwayatDonasi > 0):
    #     self.pageRiwayatDonasi -= 1
    #     print("page: ", self.pageRiwayatDonasi)
    #     self.setUpDisplayRiwayatDonasi()
    # else:
    #     print("No more RiwayatDonasi")

  def goToLamanEksplor(self):
    self.channel.emit()
  
# if __name__ == "__main__":
#   app = QApplication(sys.argv)
#   window = RiwayatDonasiWindow()
#   window.show()
#   sys.exit(app.exec())