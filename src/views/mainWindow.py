import sys, requests, json
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton
from PyQt6.QtGui import QFont, QPixmap, QCursor, QImage
from PyQt6.QtCore import Qt
from PyQt6.QtCore import pyqtSignal
import urllib.request
from requests.auth import HTTPBasicAuth

import sys
import urllib.request

graybg = '#F2F4F7'
ungu = 'rgba(90, 79, 243, 1)'
white = 'rgba(255, 255, 255, 1)'
tulisan = 'rgba(37, 49, 60, 1)'

class MainWindow(QWidget):
  channel = pyqtSignal(str, int)

  session = {
		"username-email": "",
		"password": "",
	}
    
  def setSession(self, usernameEmail, password):
    self.session["username-email"] = usernameEmail
    self.session["password"] = password

  idLaman = {
    "id-laman": -1
  }
  
  def __init__ (self):
    super().__init__()
    self.setUpMainWindow()
    
  def setUpMainWindow(self):
    self.setFixedSize(1440, 1024)
    self.setWindowTitle("KITASABI - Laman Utama")
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
        padding: 11px 30px 11px 30px;
        border: 2px solid rgba(90, 79, 243, 1);
        border-radius: 20px;
        color: rgba(37, 49, 60, 1);
        background-color: #FFFFFF;
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
  
    # Set up font
    mulish16 = QFont()
    mulish16.setFamily("Mulish"); mulish16.setPixelSize(16)
    
    mulish24 = QFont()
    mulish24.setFamily("Mulish"); mulish24.setPixelSize(24)
    
    mulish44 = QFont()
    mulish44.setFamily("Mulish"); mulish44.setPixelSize(44)
    mulish44.setBold(True)
      
    # Kata Kata Motivasi
    heading = QLabel(self)
    heading.setFixedSize(741, 253)
    heading.setStyleSheet(f'background-color: {graybg}')
    heading.move(344,79)
    
    kata_kata = QLabel(self)
    kata_kata.setText("BERSAMA, KITA SABI")
    kata_kata.move(490,138)
    kata_kata.setFont(mulish44)

    # tombol mulai penggalangan dana
    self.mulai_penggalangan_button = QPushButton(self)
    self.mulai_penggalangan_button.setText("Mulai Penggalangan Dana")
    self.mulai_penggalangan_button.setFixedSize(430, 53)
    self.mulai_penggalangan_button.move(505,239)
    self.mulai_penggalangan_button.setFont(mulish16)
    self.mulai_penggalangan_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
    self.mulai_penggalangan_button.clicked.connect(self.goToPenggalanganDana)
    
    # frame list penggalangan dana
    # background
    bg_list = QLabel(self)
    bg_list.setFixedSize(1151, 163)
    bg_list.setStyleSheet(f'background-color: {graybg}')
    bg_list.move(144,364)
    for i in range(1,2):      
      # Preview penggalangan dana +i *185
      self.preview_penggalangan_dana = QLabel(self)
      self.preview_penggalangan_dana.setText("Preview Penggalangan Dana")
      self.preview_penggalangan_dana.setStyleSheet('color: rgba(37, 49, 60, 1)')
      self.preview_penggalangan_dana.move(351, 399) 
      self.preview_penggalangan_dana.setFont(mulish24)
      # target penggalangan dana
      self.target_penggalangan = QLabel(self)
      self.target_penggalangan.setText("Nominal Target")
      self.target_penggalangan.setStyleSheet('color: rgba(37, 49, 60, 1)')
      self.target_penggalangan.move(351, 449)
      self.target_penggalangan.setFont(mulish16)
      # foto          
      url2 = 'https://yt3.ggpht.com/ytc/AKedOLQU2qqsQIYjE4SgWbHOYL4QkPO6dEXBcV8SnYEDig=s900-c-k-c0x00ffffff-no-rj'
      data2 = urllib.request.urlopen(url2).read()
      image2 = QImage()
      image2.loadFromData(data2)
      self.preview_image = QLabel(self)
      self.preview_image.setFixedSize(140, 132)
      self.preview_image.move(160, 379)
      self.preview_image.setScaledContents(True)
      pixmap2 = QPixmap(image2)
      self.preview_image.setPixmap(pixmap2)
      
      # tombol lihat detail
      self.lihat_detail_button = QPushButton(self)
      self.lihat_detail_button.setText("Lihat Detail")
      self.lihat_detail_button.setFixedSize(198, 63)
      self.lihat_detail_button.move(1009, 413)
      self.lihat_detail_button.setFont(mulish16)
      self.lihat_detail_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
      self.lihat_detail_button.clicked.connect(self.goToLihatDetail)
      
      # Ubah Data Button
      self.ubahDataButton = QPushButton(self)
      self.ubahDataButton.setText("Ubah Data")
      self.ubahDataButton.move(379, 680)
      self.ubahDataButton.setFixedSize(165,52)
      self.ubahDataButton.setFont(mulish16)
      self.ubahDataButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
      self.ubahDataButton.clicked.connect(self.goToPengelolaanAkun)
      
      # laman riwayat penggalang button
      self.riwayatPenggalangButton = QPushButton(self)
      self.riwayatPenggalangButton.setText("Riwayat Penggalang")
      self.riwayatPenggalangButton.move(634, 680)
      self.riwayatPenggalangButton.setFixedSize(165,52)
      self.riwayatPenggalangButton.setFont(mulish16)
      self.riwayatPenggalangButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
      self.riwayatPenggalangButton.clicked.connect(self.goToRiwayatPenggalanganDana)
      
      # laman riwayat penggalang button
      self.riwayatDonasiButton = QPushButton(self)
      self.riwayatDonasiButton.setText("Riwayat Donasi")
      self.riwayatDonasiButton.move(634-261-261, 680)
      self.riwayatDonasiButton.setFixedSize(165,52)
      self.riwayatDonasiButton.setFont(mulish16)
      self.riwayatDonasiButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
      self.riwayatDonasiButton.clicked.connect(self.goToRiwayatDonasi)
 
      
      # logout button
      self.logoutButton = QPushButton(self)
      self.logoutButton.setText("Logout")
      self.logoutButton.move(895, 680)
      self.logoutButton.setFixedSize(165,52)
      self.logoutButton.setFont(mulish16)
      self.logoutButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
      self.logoutButton.clicked.connect(self.goToLogout)
      
      # permintaan button
      self.permintaanButton = QPushButton(self)
      self.permintaanButton.setText("Permintaan")
      self.permintaanButton.move(895+261, 680)
      self.permintaanButton.setFixedSize(165,52)
      self.permintaanButton.setFont(mulish16)
      self.permintaanButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
      self.logoutButton.clicked.connect(self.goToPermintaan)
                                       
      #  Tombol explore lebih banyak penggalangan dana
      self.explore_button = QPushButton(self)
      self.explore_button.setText("Explore Lebih Banyak Penggalangan Dana")
      self.explore_button.setFixedSize(442, 53)
      self.explore_button.move(499, 564)
      self.explore_button.setFont(mulish16)
      self.explore_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
      self.explore_button.clicked.connect(self.goToLamanEksplor)

  def setLaman(self):
    response = requests.get('http://localhost:3000/laman/eksplor-total-donasi',
      auth=HTTPBasicAuth(self.session["username-email"], self.session["password"])
    )
    if (response.status_code == 200):
      # get list of laman (dictionary)
      listRes = json.loads(response.text)
      # get laman 1
      dictRes1 = (listRes[0])
      # set id laman
      self.idLaman["id-laman"] = dictRes1["id-laman"]
      # set judul
      self.preview_penggalangan_dana.setText(dictRes1["judul"])
      # set image
      url = dictRes1["foto-laman"][0][0]
      data = urllib.request.urlopen(url).read()
      image = QImage()
      image.loadFromData(data)
      pixmap = QPixmap(image)
      self.preview_image.setPixmap(pixmap)
      # set target
      self.target_penggalangan.setText(str(dictRes1["target"]))
    else:
      # placeholder data
      self.preview_penggalangan_dana.setText("Placeholder Title")
      url = 'https://yt3.ggpht.com/ytc/AKedOLQU2qqsQIYjE4SgWbHOYL4QkPO6dEXBcV8SnYEDig=s900-c-k-c0x00ffffff-no-rj'
      data = urllib.request.urlopen(url).read()
      image = QImage()
      image.loadFromData(data)
      pixmap = QPixmap(image)
      self.preview_image.setPixmap(pixmap)
      self.target_penggalangan.setText("Placeholder Target")
      return False
  
  def goToLamanEksplor(self):
    self.channel.emit("eksplor", -1)
  
  def goToLihatDetail(self):
    self.channel.emit("lihat_detail", self.idLaman["id-laman"])
  
  def goToPengelolaanAkun(self):
    self.channel.emit("pengelolaan_akun", -1)

  def goToPenggalanganDana(self):
    self.channel.emit("mulai_penggalang", -1)
    
  def goToRiwayatDonasi(self):
    self.channel.emit("riwayat_donasi", -1)
    
  def goToRiwayatPenggalanganDana(self):
    self.channel.emit("riwayat_penggalangan_dana", -1)

  def goToLogout(self):
    self.channel.emit("logout", -1)
  
  def goToPermintaan(self):
    self.channel.emit("permintaan", -1)
    
  
  
        

# if __name__ == "__main__":
#   app = QApplication(sys.argv)
#   window = MainWindow()
#   window.show()
#   sys.exit(app.exec())