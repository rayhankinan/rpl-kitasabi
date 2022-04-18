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

class RiwayatPenggalanganWindow(QWidget):
  switch = pyqtSignal(str, dict)

  def __init__(self):
    super().__init__()
    self.pageRiwayatPenggalangan = 0
    self.setUpRiwayatPenggalanganWindow()
    
  def setUpRiwayatPenggalanganWindow(self):
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
    self.initializeRiwayatPenggalangan()
    self.setUpDisplayRiwayatPenggalangan()
    
    # next button
    nextButton = QPushButton(self)
    nextButton.setText(">")
    nextButton.setFixedSize(40, 71)
    nextButton.move(1339,666)
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
    # nextButton.clicked.connect(self.nextRiwayatPenggalangan())
    
    # previous button
    previousButton = QPushButton(self)
    previousButton.setText("<")
    previousButton.setFixedSize(40, 71)
    previousButton.move(84,673)
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
    # previousButton.clicked.connect(self.previousRiwayatPenggalangan())    

  def initializeRiwayatPenggalangan(self):
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
    
    self.penggalanganDanaCard = []
    for i in range(3):
        self.penggalanganDanaCard.append({})
        # set preview penggalangan dana
        self.penggalanganDanaCard[i]["bg_list"] = QLabel(self)
        self.penggalanganDanaCard[i]["bg_list"].setFixedSize(956, 144)
        self.penggalanganDanaCard[i]["bg_list"].setStyleSheet(f'background-color: {graybg}')
        self.penggalanganDanaCard[i]["bg_list"].move(271,474 + i * 167)
        # Preview penggalangan dana +i *185
        self.penggalanganDanaCard[i]["judul_penggalangan_dana"] = QLabel(self)
        self.penggalanganDanaCard[i]["judul_penggalangan_dana"].setText("Judul Penggalangan Dana")
        self.penggalanganDanaCard[i]["judul_penggalangan_dana"].setStyleSheet('color: rgba(37, 49, 60, 1)')
        self.penggalanganDanaCard[i]["judul_penggalangan_dana"].setStyleSheet('background-color: #F2F4F7')
        self.penggalanganDanaCard[i]["judul_penggalangan_dana"].move(443, 505+ i * 167) 
        self.penggalanganDanaCard[i]["judul_penggalangan_dana"].setFont(mulish24)
        # nominal penggalangan dana
        self.penggalanganDanaCard[i]["nominal"] = QLabel(self)
        self.penggalanganDanaCard[i]["nominal"].setText("Nominal")
        self.penggalanganDanaCard[i]["nominal"].setStyleSheet('color: rgba(37, 49, 60, 1)')
        self.penggalanganDanaCard[i]["nominal"].setStyleSheet('background-color: #F2F4F7')
        self.penggalanganDanaCard[i]["nominal"].move(443, 549+ i * 167)
        self.penggalanganDanaCard[i]["nominal"].setFont(mulish24)
        # foto          
        url2 = 'https://yt3.ggpht.com/ytc/AKedOLQU2qqsQIYjE4SgWbHOYL4QkPO6dEXBcV8SnYEDig=s900-c-k-c0x00ffffff-no-rj'
        data2 = urllib.request.urlopen(url2).read()
        image2 = QImage()
        image2.loadFromData(data2)
        self.penggalanganDanaCard[i]["previewImg2"] = QLabel(self)
        self.penggalanganDanaCard[i]["previewImg2"].setFixedSize(117, 117)
        self.penggalanganDanaCard[i]["previewImg2"].move(287, 487+ i * 167)
        self.penggalanganDanaCard[i]["previewImg2"].setScaledContents(True)
        pixmap2 = QPixmap(image2)
        self.penggalanganDanaCard[i]["previewImg2"].setPixmap(pixmap2)
        # cairkan button
        self.penggalanganDanaCard[i]["cairkan_button"] = QPushButton(self)
        self.penggalanganDanaCard[i]["cairkan_button"].setText("Cairkan")
        self.penggalanganDanaCard[i]["cairkan_button"].setFixedSize(165, 56)
        self.penggalanganDanaCard[i]["cairkan_button"].move(990, 518+ i * 167)
        self.penggalanganDanaCard[i]["cairkan_button"].setFont(mulish24)
        self.penggalanganDanaCard[i]["cairkan_button"].setStyleSheet('''
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
        self.penggalanganDanaCard[i]["cairkan_button"].setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
  def setUpDisplayRiwayatPenggalangan(self):
    start = self.pageRiwayatPenggalangan * 3
    # for i in range(3):
    #   # if start + i < len(self.databaseRiwayatPenggalangan):
    #     # Preview penggalangan dana +i *185
    #     self.penggalanganDanaCard[i]["preview_penggalangan_dana"].setText("Judul Penggalangan Dana")
    #     # nominal penggalangan dana
    #     self.penggalanganDanaCard[i]["nominal"].setText("Nominal")
    #     # foto          
    #     self.url2 = 'https://yt3.ggpht.com/ytc/AKedOLQU2qqsQIYjE4SgWbHOYL4QkPO6dEXBcV8SnYEDig=s900-c-k-c0x00ffffff-no-rj'   
      
  
  def nextRiwayatPenggalangan(self):
    print("Right button clicked")
    # if (self.pageRiwayatPenggalangan + 1 < (len(self.databaseRiwayatPenggalangan)//3)):
    #     self.pageRiwayatPenggalangan += 1
    #     print("page: ", self.pageRiwayatPenggalangan)
    #     self.setUpDisplayRiwayatPenggalangan()
    # else:
    #     print("No more RiwayatPenggalangan")

  def previousRiwayatPenggalangan(self):
    print("Left button clicked")
    # if (self.pageRiwayatPenggalangan > 0):
    #     self.pageRiwayatPenggalangan -= 1
    #     print("page: ", self.pageRiwayatPenggalangan)
    #     self.setUpDisplayRiwayatPenggalangan()
    # else:
    #     print("No more RiwayatPenggalangan")
    
    
if __name__ == "__main__":
  app = QApplication(sys.argv)
  window = RiwayatPenggalanganWindow()
  window.show()
  sys.exit(app.exec())