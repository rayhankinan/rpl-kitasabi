import sys
from PyQt6.QtWidgets import QApplication, QWidget, QTextEdit, QLabel, QLineEdit, QPushButton, QMessageBox
from PyQt6.QtGui import QFont, QPixmap, QCursor, QImage
from PyQt6.QtCore import Qt
from PyQt6.QtCore import pyqtSignal
import sys, requests, json
from views.custom_widgets import ClickableLabel
from requests.auth import HTTPBasicAuth
import urllib.request

import sys
import urllib.request

graybg = '#F2F4F7'
ungu = 'rgba(90, 79, 243, 1)'
white = 'rgba(255, 255, 255, 1)'
tulisan = 'rgba(37, 49, 60, 1)'
pad =200

class RiwayatDonasiWindow(QWidget):
  channel = pyqtSignal()

  session = {
		"username-email": "",
		"password": "",
	}
    
  def setSession(self, usernameEmail, password):
    self.session["username-email"] = usernameEmail
    self.session["password"] = password
  
  idLaman = {
    "laman1": -1,
    "laman2": -1,
  }

  def __init__(self):
    super().__init__()
    self.pageRiwayatDonasi = 0
    self.setUpRiwayatDonasiWindow()
    
  def setUpRiwayatDonasiWindow(self):
    self.setFixedSize(1440, 1024)
    self.setWindowTitle("KITASABI - Laman Riwayat Donasi")
    self.setUpWidgets()
    
  def setUpWidgets(self):
    self.setStyleSheet('''
        QWidget {
            background-color: #E5E5E5;
        }
        QLabel {
            color: #25313C;
            font-weight: extra-bold;
            background: transparent;
        }
        QLineEdit {
            background: white;
            font-size: 12px;
            padding: 0 10 0 10
        }
        QTextEdit {
            border: 0;
            background: transparent;
            font-size: 24px;
            font-weight: bold;
            color: #25313C;
        }
        QPushButton {
            color: #ffffff;
            background-color: #5A4FF3;
            border: 1px solid #5A4FF3;
            border-radius: 12px;
            font-weight: bold;
        }
        QPushButton:hover {
            background-color: #6b75ff;
        }
    ''')
    
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
    self.returnButton.setFixedSize(208, 36)
    self.returnButton.move(33, 30)  

    self.initializeRiwayatDonasi()
    # self.setUpDisplayRiwayatDonasi()
    self.returnButton.clicked.connect(self.goToLamanEksplor)
    
    # next button
    nextButton = QPushButton(self)
    nextButton.setText(">")
    nextButton.setFixedSize(40, 71)
    nextButton.move(1336,426)
    nextButton.setFont(mulish44)
    nextButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
    # nextButton.clicked.connect(self.nextRiwayatDonasi())
    
    # previous button
    previousButton = QPushButton(self)
    previousButton.setText("<")
    previousButton.setFixedSize(40, 71)
    previousButton.move(76,426)
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
    
    # card 1
    self.labelRiwayatDonasi1 = QLabel(self)
    self.labelRiwayatDonasi1.setText("Riwayat Donasi")
    # align center text
    self.labelRiwayatDonasi1.setAlignment(Qt.AlignmentFlag.AlignCenter)
    self.labelRiwayatDonasi1.setFont(mulish33_bold)
    self.labelRiwayatDonasi1.setStyleSheet('background-color: rgba(187, 200, 212, 1)')
    self.labelRiwayatDonasi1.setFixedSize(508,63)
    self.labelRiwayatDonasi1.move(485, 72)

    # set background
    self.cardBackground1 = QLabel(self)
    self.cardBackground1.setFixedSize(1220, 558)
    self.cardBackground1.move(116, 208)
    self.cardBackground1.setStyleSheet('background-color: rgba(187, 200, 212, 1)')
    
    # set preview penggalangan dana
    self.bg_list1 = QLabel(self)
    self.bg_list1.setFixedSize(956, 128)
    self.bg_list1.setStyleSheet(f'background-color: {graybg}')
    self.bg_list1.move(253,239)
      # Preview penggalangan dana +i *185
    self.preview_penggalangan_dana1 = QLabel(self)
    self.preview_penggalangan_dana1.setText("Judul Penggalangan Dana")
    self.preview_penggalangan_dana1.setStyleSheet('color: rgba(37, 49, 60, 1)')
    self.preview_penggalangan_dana1.setStyleSheet('background-color: #F2F4F7')
    self.preview_penggalangan_dana1.move(425, 273) 
    self.preview_penggalangan_dana1.setFont(mulish24)
    # nominal penggalangan dana
    self.nominal1 = QLabel(self)
    self.nominal1.setText("Nominal")
    self.nominal1.setStyleSheet('color: rgba(37, 49, 60, 1)')
    self.nominal1.setStyleSheet('background-color: #F2F4F7')
    self.nominal1.move(425, 322)
    self.nominal1.setFont(mulish16)
    
    self.url1 = 'https://yt3.ggpht.com/ytc/AKedOLQU2qqsQIYjE4SgWbHOYL4QkPO6dEXBcV8SnYEDig=s900-c-k-c0x00ffffff-no-rj'
    self.data1 = urllib.request.urlopen(self.url1).read()
    self.image1 = QImage()
    self.image1.loadFromData(self.data1)
    self.previewImg1 = QLabel(self)
    self.previewImg1.setFixedSize(117, 98)
    self.previewImg1.move(269, 253)
    self.previewImg1.setScaledContents(True)
    self.pixmap1 = QPixmap(self.image1)
    self.previewImg1.setPixmap(self.pixmap1)
    
    # card 2
    # set background
    self.cardBackground2 = QLabel(self)
    self.cardBackground2.setFixedSize(1220, 558)
    self.cardBackground2.move(116, 208+185)
    self.cardBackground2.setStyleSheet('background-color: rgba(187, 200, 212, 1)')
    
    # set preview penggalangan dana
    self.bg_list2 = QLabel(self)
    self.bg_list2.setFixedSize(956, 128)
    self.bg_list2.setStyleSheet(f'background-color: {graybg}')
    self.bg_list2.move(253,239+185)
      # Preview penggalangan dana +i *185
    self.preview_penggalangan_dana2 = QLabel(self)
    self.preview_penggalangan_dana2.setText("Judul Penggalangan Dana")
    self.preview_penggalangan_dana2.setStyleSheet('color: rgba(37, 49, 60, 1)')
    self.preview_penggalangan_dana2.setStyleSheet('background-color: #F2F4F7')
    self.preview_penggalangan_dana2.move(425, 273+185) 
    self.preview_penggalangan_dana2.setFont(mulish24)
    # nominal penggalangan dana
    self.nominal2 = QLabel(self)
    self.nominal2.setText("Nominal")
    self.nominal2.setStyleSheet('color: rgba(37, 49, 60, 1)')
    self.nominal2.setStyleSheet('background-color: #F2F4F7')
    self.nominal2.move(425, 322+185)
    self.nominal2.setFont(mulish16)
    # foto          
    self.url2 = 'https://yt3.ggpht.com/ytc/AKedOLQU2qqsQIYjE4SgWbHOYL4QkPO6dEXBcV8SnYEDig=s900-c-k-c0x00ffffff-no-rj'
    self.data2 = urllib.request.urlopen(self.url2).read()
    self.image2 = QImage()
    self.image2.loadFromData(self.data2)
    self.previewImg2 = QLabel(self)
    self.previewImg2.setFixedSize(117, 98)
    self.previewImg2.move(269, 253+185)
    self.previewImg2.setScaledContents(True)
    self.pixmap2 = QPixmap(self.image2)
    self.previewImg2.setPixmap(self.pixmap2)

  def setLaman(self):
    response = requests.get('http://localhost:3000/transaksi/riwayat-donatur',
      auth=HTTPBasicAuth(self.session["username-email"], self.session["password"])
    )
    if (response.status_code == 200):
      listRes = json.loads(response.text)
      dictRes1 = (listRes[0])
      
      self.idLaman["laman1"] = dictRes1["id-laman"]
      response_laman = requests.get('http://localhost:3000/laman/detail-laman', data={"id-laman": dictRes1["id-laman"]},
        auth=HTTPBasicAuth(self.session["username-email"], self.session["password"])
      )
      lamanRes = json.loads(response_laman.text)
      self.preview_penggalangan_dana1.setText(lamanRes["judul"])
      self.nominal1.setText(str(dictRes1["jumlah-transaksi"]))
      self.url1 = lamanRes["foto-laman"][0][0]
      self.data1 = urllib.request.urlopen(self.url1).read()
      self.image1 = QImage()
      self.image1.loadFromData(self.data1)
      self.previewImg1 = QLabel(self)
      self.previewImg1.setFixedSize(117, 98)
      self.previewImg1.move(269, 253)
      self.previewImg1.setScaledContents(True)
      self.pixmap1 = QPixmap(self.image1)
      self.previewImg1.setPixmap(self.pixmap1)
       
      if (len(listRes) >= 2):
        dictRes2 = (listRes[1])    
        self.idLaman["laman2"] = dictRes2["id-laman"]
        response_laman = requests.get('http://localhost:3000/laman/detail-laman', data={"id-laman": dictRes2["id-laman"]},
          auth=HTTPBasicAuth(self.session["username-email"], self.session["password"])
        )
        lamanRes = json.loads(response_laman.text)
        self.preview_penggalangan_dana2.setText(lamanRes["judul"])
        self.nominal2.setText(str(dictRes2["jumlah-transaksi"]))
        self.url2 = lamanRes["foto-laman"][0][0]
        self.data2 = urllib.request.urlopen(self.url2).read()
        self.image2 = QImage()
        self.image2.loadFromData(self.data2)
        self.previewImg2 = QLabel(self)
        self.previewImg2.setFixedSize(117, 98)
        self.previewImg2.move(269, 253+185)
        self.previewImg2.setScaledContents(True)
        self.pixmap2 = QPixmap(self.image2)
        self.previewImg2.setPixmap(self.pixmap2)         

  def goToLamanEksplor(self):
    self.channel.emit()
  
# if __name__ == "__main__":
#   app = QApplication(sys.argv)
#   window = RiwayatDonasiWindow()
#   window.show()
#   sys.exit(app.exec())