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

class MainWindow(QWidget):
  channel = pyqtSignal(str)
  
  def __init__ (self):
    super().__init__()
    self.setUpMainWindow()
    
  def setUpMainWindow(self):
    self.setFixedSize(1440, 1024)
    self.setWindowTitle("KITASABI - Laman Utama")
    self.setUpWidgets()
    
  
  def setUpWidgets(self):
    # Set warna background
    self.setStyleSheet('background-color: #E5E5E5')
  
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
    heading.setFixedSize(1151, 253)
    heading.setStyleSheet(f'background-color: {graybg}')
    heading.move(144,79)
    
    kata_kata = QLabel(self)
    kata_kata.setText("Tidak Perlu Kata-Kata Yang Penting Bukti Nyata")
    kata_kata.setStyleSheet('''
      color: #25313C;
      font-weight: extra-bold;
      background-color: #F2F4F7
    ''')
    kata_kata.move(230,138)
    kata_kata.setFont(mulish44)
    

    
    # tombol mulai penggalangan dana
    self.mulai_penggalangan_button = QPushButton(self)
    self.mulai_penggalangan_button.setText("Mulai Penggalangan Dana")
    self.mulai_penggalangan_button.setFixedSize(430, 53)
    self.mulai_penggalangan_button.move(505,239)
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
      self.preview_penggalangan_dana.setStyleSheet('background-color: #F2F4F7')
      self.preview_penggalangan_dana.move(351, 399) 
      self.preview_penggalangan_dana.setFont(mulish24)
      # target penggalangan dana
      self.target_penggalangan = QLabel(self)
      self.target_penggalangan.setText("Nominal Target")
      self.target_penggalangan.setStyleSheet('color: rgba(37, 49, 60, 1)')
      self.target_penggalangan.setStyleSheet('background-color: #F2F4F7')
      self.target_penggalangan.move(351, 449)
      self.target_penggalangan.setFont(mulish24)
      # foto          
      url2 = 'https://yt3.ggpht.com/ytc/AKedOLQU2qqsQIYjE4SgWbHOYL4QkPO6dEXBcV8SnYEDig=s900-c-k-c0x00ffffff-no-rj'
      data2 = urllib.request.urlopen(url2).read()
      image2 = QImage()
      image2.loadFromData(data2)
      self.previewImg2 = QLabel(self)
      self.previewImg2.setFixedSize(140, 132)
      self.previewImg2.move(160, 379)
      self.previewImg2.setScaledContents(True)
      pixmap2 = QPixmap(image2)
      self.previewImg2.setPixmap(pixmap2)
      
      # tombol lihat detail
      self.lihat_detail_button = QPushButton(self)
      self.lihat_detail_button.setText("Lihat Detail")
      self.lihat_detail_button.setFixedSize(198, 63)
      self.lihat_detail_button.move(1009, 413)
      self.lihat_detail_button.setFont(mulish16)
      self.lihat_detail_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
      self.lihat_detail_button.setStyleSheet('''
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
      self.lihat_detail_button.clicked.connect(self.goToLihatDetail)
      
      # Ubah Data Button
      self.ubahDataButton = QPushButton(self)
      self.ubahDataButton.setText("Ubah Data")
      self.ubahDataButton.move(379, 680)
      self.ubahDataButton.setFixedSize(165,52)
      self.ubahDataButton.setFont(mulish16)
      self.ubahDataButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
      self.ubahDataButton.setStyleSheet('''
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
      self.ubahDataButton.clicked.connect(self.goToPengelolaanAkun)
      
      # laman riwayat button
      self.lamanRiwayatButton = QPushButton(self)
      self.lamanRiwayatButton.setText("Laman Riwayat")
      self.lamanRiwayatButton.move(634, 680)
      self.lamanRiwayatButton.setFixedSize(165,52)
      self.lamanRiwayatButton.setFont(mulish16)
      self.lamanRiwayatButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
      self.lamanRiwayatButton.setStyleSheet('''
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
      self.lamanRiwayatButton.clicked.connect(self.goToRiwayatPenggalanganDana)
      
      # logout button
      self.logoutButton = QPushButton(self)
      self.logoutButton.setText("Logout")
      self.logoutButton.move(895, 680)
      self.logoutButton.setFixedSize(165,52)
      self.logoutButton.setFont(mulish16)
      self.logoutButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
      self.logoutButton.setStyleSheet('''
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
      self.logoutButton.clicked.connect(self.goToLogout)
                                       
      #  Tombol explore lebih banyak penggalangan dana
      self.explore_button = QPushButton(self)
      self.explore_button.setText("Explore Lebih Banyak Penggalangan Dana")
      self.explore_button.setFixedSize(442, 53)
      self.explore_button.move(499, 564)
      self.explore_button.setFont(mulish16)
      self.explore_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
      self.explore_button.setStyleSheet('''
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
      self.explore_button.clicked.connect(self.goToLamanEksplor)
  
  def goToLamanEksplor(self):
    self.channel.emit("eksplor")
  
  def goToLihatDetail(self):
    self.channel.emit("lihat_detail")
  
  def goToPengelolaanAkun(self):
    self.channel.emit("pengelolaan_akun")

  def goToPenggalanganDana(self):
    self.channel.emit("mulai_penggalang")
    
  def goToRiwayatDonasi(self):
    self.channel.emit("riwayat_donasi")
    
  def goToRiwayatPenggalanganDana(self):
    self.channel.emit("riwayat_penggalangan_dana")

  def goToLogout(self):
    self.channel.emit("logout")
  
  def goToPermintaan(self):
    self.channel.emit("permintaan")
    
  
  
        

# if __name__ == "__main__":
#   app = QApplication(sys.argv)
#   window = MainWindow()
#   window.show()
#   sys.exit(app.exec())