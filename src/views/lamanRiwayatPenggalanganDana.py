import sys
from urllib import response
from PyQt6.QtWidgets import QApplication, QWidget, QTextEdit, QLabel, QLineEdit, QPushButton, QMessageBox
from PyQt6.QtGui import QFont, QPixmap, QCursor, QImage
from PyQt6.QtCore import Qt
from PyQt6.QtCore import pyqtSignal
from views.custom_widgets import ClickableLabel
import urllib.request
import sys, requests, json
import sys
import urllib.request

graybg = '#F2F4F7'
ungu = 'rgba(90, 79, 243, 1)'
white = 'rgba(255, 255, 255, 1)'
tulisan = 'rgba(37, 49, 60, 1)'

class RiwayatPenggalanganWindow(QWidget):
  channel = pyqtSignal(str)
  
  idLaman = {
    "laman1": -1,
    "laman2": -1,
  }

  def __init__(self):
    super().__init__()
    self.pageRiwayatPenggalangan = 0
    self.setUpRiwayatPenggalanganWindow()
    
  def setUpRiwayatPenggalanganWindow(self):
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

    self.initializeRiwayatPenggalangan()
    self.setUpDisplayRiwayatPenggalangan()
    self.returnButton.clicked.connect(self.goToLamanEksplor)
    
    # next button
    nextButton = QPushButton(self)
    nextButton.setText(">")
    nextButton.setFixedSize(40, 71)
    nextButton.move(1339,466)
    nextButton.setFont(mulish44)
    nextButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
    # nextButton.clicked.connect(self.nextRiwayatPenggalangan())
    
    # previous button
    previousButton = QPushButton(self)
    previousButton.setText("<")
    previousButton.setFixedSize(40, 71)
    previousButton.move(84,466)  
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
    self.labelRiwayatPenggalanganDana1 = QLabel(self)
    self.labelRiwayatPenggalanganDana1.setText("Riwayat Penggalangan Dana")
    # align center text
    self.labelRiwayatPenggalanganDana1.setAlignment(Qt.AlignmentFlag.AlignCenter)
    self.labelRiwayatPenggalanganDana1.setFont(mulish33_bold)
    self.labelRiwayatPenggalanganDana1.setStyleSheet('background-color: rgba(187, 200, 212, 1)')
    self.labelRiwayatPenggalanganDana1.setFixedSize(508,63)
    self.labelRiwayatPenggalanganDana1.move(495, 72)

    # Mulai Penggalangan Dana Button
    # tombol mulai penggalangan dana
    self.mulai_penggalangan_button1 = QPushButton(self)
    self.mulai_penggalangan_button1.setText("Mulai Penggalangan Dana")
    self.mulai_penggalangan_button1.setFixedSize(321, 56)
    self.mulai_penggalangan_button1.move(602,169)
    self.mulai_penggalangan_button1.setFont(mulish16)
    self.mulai_penggalangan_button1.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
    self.mulai_penggalangan_button1.clicked.connect(self.goToLamanPenggalang)
    
    # set background
    self.cardBackground1 = QLabel(self)
    self.cardBackground1.setFixedSize(1220, 506)
    self.cardBackground1.move(124, 270)
    self.cardBackground1.setStyleSheet('background-color: rgba(187, 200, 212, 1)')
    
    # set preview penggalangan dana
    self.bg_list1 = QLabel(self)
    self.bg_list1.setFixedSize(956, 144)
    self.bg_list1.setStyleSheet(f'background-color: {graybg}')
    self.bg_list1.move(271,284 )
    # Preview penggalangan dana +i *185
    self.judul_penggalangan_dana1 = QLabel(self)
    self.judul_penggalangan_dana1.setText("Judul Penggalangan Dana")
    self.judul_penggalangan_dana1.setStyleSheet('color: rgba(37, 49, 60, 1)')
    self.judul_penggalangan_dana1.setStyleSheet('background-color: #F2F4F7')
    self.judul_penggalangan_dana1.move(443, 315) 
    self.judul_penggalangan_dana1.setFont(mulish24)
    # nominal penggalangan dana
    self.nominal1 = QLabel(self)
    self.nominal1.setText("Nominal")
    self.nominal1.setStyleSheet('color: rgba(37, 49, 60, 1)')
    self.nominal1.setStyleSheet('background-color: #F2F4F7')
    self.nominal1.move(443, 359)
    self.nominal1.setFont(mulish16)
    # foto          
    url1 = 'https://yt3.ggpht.com/ytc/AKedOLQU2qqsQIYjE4SgWbHOYL4QkPO6dEXBcV8SnYEDig=s900-c-k-c0x00ffffff-no-rj'
    data1 = urllib.request.urlopen(url1).read()
    image1 = QImage()
    image1.loadFromData(data1)
    self.previewImg1 = QLabel(self)
    self.previewImg1.setFixedSize(117, 117)
    self.previewImg1.move(287, 297)
    self.previewImg1.setScaledContents(True)
    pixmap1 = QPixmap(image1)
    self.previewImg1.setPixmap(pixmap1)
    # cairkan button
    self.cairkan_button1 = QPushButton(self)
    self.cairkan_button1.setText("Cairkan")
    self.cairkan_button1.setFixedSize(165, 56)
    self.cairkan_button1.move(990, 328)
    self.cairkan_button1.setFont(mulish16)
    self.cairkan_button1.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
    self.cairkan_button1.clicked.connect(self.cairkan1)
    
 # set preview penggalangan dana
    self.bg_list2 = QLabel(self)
    self.bg_list2.setFixedSize(956, 144)
    self.bg_list2.setStyleSheet(f'background-color: {graybg}')
    self.bg_list2.move(271,284+167 )
    # Preview penggalangan dana +i *185
    self.judul_penggalangan_dana2 = QLabel(self)
    self.judul_penggalangan_dana2.setText("Judul Penggalangan Dana")
    self.judul_penggalangan_dana2.setStyleSheet('color: rgba(37, 49, 60, 1)')
    self.judul_penggalangan_dana2.setStyleSheet('background-color: #F2F4F7')
    self.judul_penggalangan_dana2.move(443, 315+167) 
    self.judul_penggalangan_dana2.setFont(mulish24)
    # nominal penggalangan dana
    self.nominal2 = QLabel(self)
    self.nominal2.setText("Nominal")
    self.nominal2.setStyleSheet('color: rgba(37, 49, 60, 1)')
    self.nominal2.setStyleSheet('background-color: #F2F4F7')
    self.nominal2.move(443, 359+167)
    self.nominal2.setFont(mulish16)
    # foto          
    url2 = 'https://yt3.ggpht.com/ytc/AKedOLQU2qqsQIYjE4SgWbHOYL4QkPO6dEXBcV8SnYEDig=s900-c-k-c0x00ffffff-no-rj'
    data2 = urllib.request.urlopen(url2).read()
    image2 = QImage()
    image2.loadFromData(data2)
    self.previewImg2 = QLabel(self)
    self.previewImg2.setFixedSize(117, 117)
    self.previewImg2.move(287, 297+167)
    self.previewImg2.setScaledContents(True)
    pixmap2 = QPixmap(image2)
    self.previewImg2.setPixmap(pixmap2)
    # cairkan button
    self.cairkan_button2 = QPushButton(self)
    self.cairkan_button2.setText("Cairkan")
    self.cairkan_button2.setFixedSize(165, 56)
    self.cairkan_button2.move(990, 328+167)
    self.cairkan_button2.setFont(mulish16)
    self.cairkan_button2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
    self.cairkan_button2.clicked.connect(self.cairkan2)    

  def setLaman(self):
      response = requests.get('http://localhost:3000/riwayat-laman')
      if (response.status_code == 200):
          listRes = json.loads(response.text)
          dictRes1 = (listRes[0])
          
          self.idLaman["laman1"] = dictRes1["id-laman"]
          self.judul_penggalangan_dana1.setText(dictRes1["judul"])
          self.nominal1.setText(dictRes1["total-donasi"])
          url1 = dictRes1["foto-laman"][0][0]
          data1 = urllib.request.urlopen(url1).read()
          image1 = QImage()
          image1.loadFromData(data1)
          self.previewImg1 = QLabel(self)
          self.previewImg1.setFixedSize(117, 117)
          self.previewImg1.move(287, 297)
          self.previewImg1.setScaledContents(True)
          pixmap1 = QPixmap(image1)
          self.previewImg1.setPixmap(pixmap1)
          
          if(len(listRes) >= 2):
            dictRes2 = (listRes[1])    
            self.idLaman["laman2"] = dictRes2["idLaman"]
            self.judul_penggalangan_dana2.setText(dictRes2["judul"])
            self.nominal1.setText(str(dictRes2["jumlahTransaksi"]))
            self.url2 = dictRes2["foto-laman"][0][0]
            self.data2 = urllib.request.urlopen(self.url2).read()
            self.image2 = QImage()
            self.image2.loadFromData(self.data2)
            self.previewImg2 = QLabel(self)
            self.previewImg2.setFixedSize(117, 117)
            self.previewImg2.move(287, 297+167)
            self.previewImg2.setScaledContents(True)
            self.pixmap2 = QPixmap(self.image2)
            self.previewImg2.setPixmap(self.pixmap2)
            return True
      else:
            return False
                        
    
    
    
  def goToLamanEksplor(self):
    self.channel.emit("eksplor")
  
  
  def cairkan1(self):
    response = requests.get('http://localhost:3000/transaksi/cair', data = self.idLaman["laman1"])
    
  def cairkan2(self):
    response = requests.get('http://localhost:3000/transaksi/cair', data = self.idLaman["laman2"])
    

  def goToLamanPenggalang(self):
    self.channel.emit("penggalang")
  
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
    
    
# if __name__ == "__main__":
#   app = QApplication(sys.argv)
#   window = RiwayatPenggalanganWindow()
#   window.show()
#   sys.exit(app.exec())