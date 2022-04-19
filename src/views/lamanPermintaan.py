import sys, requests, json
from PyQt6.QtWidgets import QApplication, QWidget, QTextEdit, QLabel, QLineEdit, QPushButton, QMessageBox
from PyQt6.QtGui import QFont, QPixmap, QCursor, QImage
from PyQt6.QtCore import Qt
from PyQt6.QtCore import pyqtSignal
import urllib.request
from requests.auth import HTTPBasicAuth

graybg = '#F2F4F7'
ungu = 'rgba(90, 79, 243, 1)'
white = 'rgba(255, 255, 255, 1)'
tulisan = 'rgba(37, 49, 60, 1)'

class LamanPermintaan(QWidget):
  channel = pyqtSignal(str)

  session = {
		"username-email": "",
		"password": "",
	}
    
  def setSession(self, usernameEmail, password):
    self.session["username-email"] = usernameEmail
    self.session["password"] = password
  
  def __init__(self):
    super().__init__()
    self.pagePermintaanDiterima = 0
    self.setUpPermintaanDiterimaWindow()
  
  def setUpPermintaanDiterimaWindow(self):
    self.setFixedSize(1440, 1024)
    self.setWindowTitle("KITASABI - Laman Permintaan Diterima")
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
    self.initializePermintaanDiterima()
    self.setUpDisplayPermintaanDiterima()
    
    # next button
    nextButton = QPushButton(self)
    nextButton.setText(">")
    nextButton.setFixedSize(40, 71)
    nextButton.move(1339,436)
    nextButton.setFont(mulish44)
    nextButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
    # nextButton.clicked.connect(self.nextPermintaanDiterima())    

    # previous button
    previousButton = QPushButton(self)
    previousButton.setText("<")
    previousButton.setFixedSize(40, 71)
    previousButton.move(84,436) 
    previousButton.setFont(mulish44)
    previousButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
    # previousButton.clicked.connect(self.previousPermintaanDiterima())                              
  
  def initializePermintaanDiterima(self):
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
    self.labelRiwayatPenggalanganDana.setFixedSize(658,73)
    self.labelRiwayatPenggalanganDana.setStyleSheet('background-color: rgba(187, 200, 212, 1)')
    self.labelRiwayatPenggalanganDana.move(410, 72)

    # Mulai Penggalangan Dana Button
    # tombol mulai penggalangan dana
    self.mulai_penggalangan_button = QPushButton(self)
    self.mulai_penggalangan_button.setText("Mulai Penggalangan Dana")
    self.labelRiwayatPenggalanganDana.setAlignment(Qt.AlignmentFlag.AlignCenter)
    self.mulai_penggalangan_button.setFixedSize(281, 46)
    self.mulai_penggalangan_button.move(622,169)
    self.mulai_penggalangan_button.setFont(mulish16)
    self.mulai_penggalangan_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
    self.mulai_penggalangan_button.clicked.connect(self.goToLamanPenggalang)
    
    # set background
    self.cardBackground = QLabel(self)
    self.cardBackground.setFixedSize(1220, 506)
    self.cardBackground.move(124, 240)
    self.cardBackground.setStyleSheet('background-color: rgba(187, 200, 212, 1)')

    # set preview penggalangan dana
    self.previewBg1 = QTextEdit(self)
    self.previewBg1.setDisabled(True)
    self.previewBg1.setFixedSize(1010, 227)
    self.previewBg1.move(233, 212)
    self.previewBg1.setStyleSheet('background-color: #FFFFFF')
    
    self.previewText1 = QTextEdit(self)
    self.previewText1.setDisabled(True)
    self.previewText1.setFixedSize(500, 130)
    self.previewText1.move(469, 262)

    self.previewImg1 = QLabel(self)
    self.previewImg1.setFixedSize(176, 176)
    self.previewImg1.move(268, 238)
    self.previewImg1.setScaledContents(True)

    # set bayar button
    self.detail1 = QPushButton(self)
    self.detail1.setText("Lihat Detail >")
    self.detail1.setFixedSize(165, 52)
    self.detail1.move(1020, 301)
    self.detail1.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
    # self.detail1.clicked.connect(self.goToLamanDetail1)

    # set preview penggalangan dana
    self.previewBg2 = QTextEdit(self)
    self.previewBg2.setDisabled(True)
    self.previewBg2.setFixedSize(1010, 227)
    self.previewBg2.move(233, 462)
    self.previewBg2.setStyleSheet('background-color: #FFFFFF')
    
    self.previewText2 = QTextEdit(self)
    self.previewText2.setFixedSize(500, 130)
    self.previewText2.setDisabled(True)
    self.previewText2.setText("Judul Penggalangan (ISI PAKE DATA)")
    self.previewText2.move(469, 512)

    self.previewImg2 = QLabel(self)
    self.previewImg2.setFixedSize(176, 176)
    self.previewImg2.move(268, 488)
    self.previewImg2.setScaledContents(True)

    # set bayar button
    self.detail2 = QPushButton(self)
    self.detail2.setText("Lihat Detail >")
    self.detail2.setFixedSize(165, 52)
    self.detail2.move(1020, 551)
    self.detail2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
    # self.detail2.clicked.connect(self.goToLamanDetail2)

    # set preview penggalangan dana
    self.previewBg3 = QTextEdit(self)
    self.previewBg3.setDisabled(True)
    self.previewBg3.setFixedSize(1010, 227)
    self.previewBg3.move(233, 212)
    self.previewBg3.setStyleSheet('background-color: #FFFFFF')
    
    self.previewText3 = QTextEdit(self)
    self.previewText3.setDisabled(True)
    self.previewText3.setFixedSize(500, 130)
    self.previewText3.move(469, 262)

    self.previewImg3 = QLabel(self)
    self.previewImg3.setFixedSize(176, 176)
    self.previewImg3.move(268, 238)
    self.previewImg3.setScaledContents(True)

    # set bayar button
    self.detail3 = QPushButton(self)
    self.detail3.setText("Lihat Detail >")
    self.detail3.setFixedSize(165, 52)
    self.detail3.move(1020, 301)
    self.detail3.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
    # self.detail3.clicked.connect(self.goToLamanDetail1)
    
  def setLaman(self):
    # response = requests.post('http://localhost:3000/permintaan/riwayat-permintaan',
    #   auth=HTTPBasicAuth(self.session["username-email"], self.session["password"])
    # )
    # if (response.status_code == 200):
    #     # get list of laman (dictionary)
    #     listRes = json.loads(response.text)
    #     # get laman 1
    #     dictRes1 = (listRes[0])
    #     # set id laman
    #     self.idLaman["laman1"] = dictRes1["id-laman"]
    #     # set judul
    #     self.previewText1.setText(str(dictRes1["judul"]))
    #     # set image
    #     url = dictRes1["foto-laman"][0][0]
    #     data = urllib.request.urlopen(url).read()
    #     image = QImage()
    #     image.loadFromData(data)
    #     pixmap = QPixmap(image)
    #     self.previewImg1.setPixmap(pixmap)
    #     # check for laman 2
    #     if (len(listRes) >= 2):
    #         # set id laman
    #         self.idLaman["laman2"] = dictRes2["id-laman"]
    #         # get laman 2
    #         dictRes2 = (listRes[1])
    #         # set judul
    #         self.previewText2.setText(dictRes2["judul"])
    #         # set image
    #         url = dictRes2["foto-laman"][0][0]
    #         data = urllib.request.urlopen(url).read()
    #         image = QImage()
    #         image.loadFromData(data)
    #         pixmap = QPixmap(image)
    #         self.previewImg2.setPixmap(pixmap)
    #         return True
    #     else:
    #         # placeholder data
    #         self.previewText2.setText("Placeholder Title")
    #         url = 'https://yt3.ggpht.com/ytc/AKedOLQU2qqsQIYjE4SgWbHOYL4QkPO6dEXBcV8SnYEDig=s900-c-k-c0x00ffffff-no-rj'
    #         data = urllib.request.urlopen(url).read()
    #         image = QImage()
    #         image.loadFromData(data)
    #         pixmap = QPixmap(image)
    #         self.previewImg2.setPixmap(pixmap)
    #         return False
    # else:
    #     # placeholder data
    #     self.previewText1.setText("Placeholder Title")
    #     url = 'https://yt3.ggpht.com/ytc/AKedOLQU2qqsQIYjE4SgWbHOYL4QkPO6dEXBcV8SnYEDig=s900-c-k-c0x00ffffff-no-rj'
    #     data = urllib.request.urlopen(url).read()
    #     image = QImage()
    #     image.loadFromData(data)
    #     pixmap = QPixmap(image)
    #     self.previewImg1.setPixmap(pixmap)
    #     return False
  
    for i in range(3):
        self.penggalanganDanaCard.append({})
        # set preview penggalangan dana
        self.penggalanganDanaCard[i]["bg_list"] = QLabel(self)
        self.penggalanganDanaCard[i]["bg_list"].setFixedSize(956, 144)
        self.penggalanganDanaCard[i]["bg_list"].setStyleSheet(f'background-color: {graybg}')
        self.penggalanganDanaCard[i]["bg_list"].move(271,254 + i * 167)
        # Preview penggalangan dana +i *185
        self.penggalanganDanaCard[i]["judul_penggalangan_dana"] = QLabel(self)
        self.penggalanganDanaCard[i]["judul_penggalangan_dana"].setText("Judul Penggalangan Dana")
        self.penggalanganDanaCard[i]["judul_penggalangan_dana"].setStyleSheet('color: rgba(37, 49, 60, 1)')
        self.penggalanganDanaCard[i]["judul_penggalangan_dana"].setStyleSheet('background-color: #F2F4F7')
        self.penggalanganDanaCard[i]["judul_penggalangan_dana"].move(443, 285+ i * 167) 
        self.penggalanganDanaCard[i]["judul_penggalangan_dana"].setFont(mulish24)
        # nominal penggalangan dana
        self.penggalanganDanaCard[i]["nominal"] = QLabel(self)
        self.penggalanganDanaCard[i]["nominal"].setText("Nominal")
        self.penggalanganDanaCard[i]["nominal"].setStyleSheet('color: rgba(37, 49, 60, 1)')
        self.penggalanganDanaCard[i]["nominal"].setStyleSheet('background-color: #F2F4F7')
        self.penggalanganDanaCard[i]["nominal"].move(443, 329+ i * 167)
        self.penggalanganDanaCard[i]["nominal"].setFont(mulish16)
        # foto          
        url2 = 'https://yt3.ggpht.com/ytc/AKedOLQU2qqsQIYjE4SgWbHOYL4QkPO6dEXBcV8SnYEDig=s900-c-k-c0x00ffffff-no-rj'
        data2 = urllib.request.urlopen(url2).read()
        image2 = QImage()
        image2.loadFromData(data2)
        self.penggalanganDanaCard[i]["previewImg2"] = QLabel(self)
        self.penggalanganDanaCard[i]["previewImg2"].setFixedSize(117, 117)
        self.penggalanganDanaCard[i]["previewImg2"].move(287, 267+ i * 167)
        self.penggalanganDanaCard[i]["previewImg2"].setScaledContents(True)
        pixmap2 = QPixmap(image2)
        self.penggalanganDanaCard[i]["previewImg2"].setPixmap(pixmap2)
        # cairkan button
        self.penggalanganDanaCard[i]["buat_laman"] = QPushButton(self)
        self.penggalanganDanaCard[i]["buat_laman"].setText("Buat Laman")
        self.penggalanganDanaCard[i]["buat_laman"].setFixedSize(165, 56)
        self.penggalanganDanaCard[i]["buat_laman"].move(990, 298+ i * 167)
        self.penggalanganDanaCard[i]["buat_laman"].setFont(mulish16)
        self.penggalanganDanaCard[i]["buat_laman"].setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.penggalanganDanaCard[i]["buat_laman"].clicked.connect(self.goToBuatLaman)
  
  def goToLamanEksplor(self):
    self.channel.emit("eksplor")
  
  def goToBuatLaman(self):
    self.channel.emit("pageBuilder")
    # do cair

  def goToLamanPenggalang(self):
    self.channel.emit("penggalang")

  def setUpDisplayPermintaanDiterima(self):
    start = self.pagePermintaanDiterima * 3
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
#   window = PermintaanDiterimaWindow()
#   window.show()
#   sys.exit(app.exec())
