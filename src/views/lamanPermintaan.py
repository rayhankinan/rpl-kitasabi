import sys, requests, json
from PyQt6.QtWidgets import QApplication, QWidget, QTextEdit, QLabel, QLineEdit, QPushButton, QMessageBox
from PyQt6.QtGui import QFont, QPixmap, QCursor, QImage, QIcon
from PyQt6.QtCore import Qt
from PyQt6.QtCore import pyqtSignal
import pathlib
from requests.auth import HTTPBasicAuth

graybg = '#F2F4F7'
ungu = 'rgba(90, 79, 243, 1)'
white = 'rgba(255, 255, 255, 1)'
tulisan = 'rgba(37, 49, 60, 1)'

class LamanPermintaan(QWidget):
  channel = pyqtSignal(str, int)

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
      
      # set overall page layout
      self.setFixedSize(1440, 1024)
      self.setWindowTitle("KITASABI - Permintaan")
      self.setStyleSheet('background-color: #F2F4F7')

      # set fonts
      mulish16 = QFont()
      mulish16.setFamily("Mulish"); mulish16.setPixelSize(16)
      mulish24 = QFont()
      mulish24.setFamily("Mulish"); mulish24.setPixelSize(24)
      mulish44 = QFont()
      mulish44.setFamily("Mulish"); mulish44.setPixelSize(44)
      self.setWidget()
      current_directory = str(pathlib.Path(__file__).parent.absolute())
      path = current_directory + '/../../img/icon.png'
      self.setWindowIcon(QIcon(path))

  def setWidget(self):
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

      self.returnButton = QPushButton(self)
      self.returnButton.setText("< Kembali ke Laman Utama")
      self.returnButton.setFixedSize(258, 36)
      self.returnButton.move(53, 32)
      self.returnButton.clicked.connect(self.goToHome)

      self.profileButton = QPushButton(self)
      self.profileButton.setFixedSize(56, 56)
      self.profileButton.move(1323, 22)
      self.profileButton.setStyleSheet('''
          QPushButton {
              padding-right: 50px;
              padding-top: 25px;
              background: #DAE3EA;
              border: 2px;
              border-radius: 28;
          }
          QPushButton:hover {
              background: #FFFFFF;
          }
      ''')
      self.profileButton.clicked.connect(self.goToEditProfil)
      
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

      # set bayar button
      self.detail1 = QPushButton(self)
      self.detail1.setFixedSize(165, 52)
      self.detail1.move(1020, 301)
      self.detail1.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
      self.detail1.clicked.connect(self.goToLamanDetail1)

      # set preview penggalangan dana
      self.previewBg2 = QTextEdit(self)
      self.previewBg2.setDisabled(True)
      self.previewBg2.setFixedSize(1010, 227)
      self.previewBg2.move(233, 462)
      self.previewBg2.setStyleSheet('background-color: #FFFFFF')
      
      self.previewText2 = QTextEdit(self)
      self.previewText2.setFixedSize(500, 130)
      self.previewText2.setDisabled(True)
      self.previewText2.move(469, 512)

      # set bayar button
      self.detail2 = QPushButton(self)
      self.detail2.setFixedSize(165, 52)
      self.detail2.move(1020, 551)
      self.detail2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
      self.detail2.clicked.connect(self.goToLamanDetail2)

  def setLaman(self):
    response = requests.get('http://localhost:3000/permintaan/riwayat-permintaan',
      auth=HTTPBasicAuth(self.session["username-email"], self.session["password"])
    )
    if (response.status_code == 200):
      # get list of laman (dictionary)
      listRes = json.loads(response.text)
      # get laman 1
      dictRes1 = (listRes[0])
      # set id laman
      self.idLaman["laman1"] = dictRes1["id-permintaan"]
      # set judul
      self.previewText1.setText(str(dictRes1["judul"]))
      # set detail
      if (dictRes1["status-autentikasi"]):
        self.detail1.setDisabled(False)
        self.detail1.setText("Buat Laman")
      else:
        self.detail1.setDisabled(True)
        self.detail1.setText("Pending")
      # check for laman 2
      if (len(listRes) >= 2):
        dictRes2 = (listRes[1])
        # set id laman
        self.idLaman["laman2"] = dictRes2["id-permintaan"]
        # get laman 2
        # set judul
        self.previewText2.setText(dictRes2["judul"])
        # set button
        if (dictRes2["status-autentikasi"]):
          self.detail2.setDisabled(False)
          self.detail2.setText("Buat Laman")
        else:
          self.detail2.setDisabled(True)
          self.detail2.setText("Pending")
        return True
      else:
        # placeholder data
        self.previewText2.setText("Not Found")
        self.detail2.setDisabled(True)
        return False
    else:
      # placeholder data
      self.previewText1.setText("Not Found")
      self.previewText2.setText("Not Found")
      self.detail1.setDisabled(True)
      self.detail2.setDisabled(True)
      return False

  def goToHome(self):
        self.channel.emit("home", -1)
        
  def goToEditProfil(self):
      self.channel.emit("profile", -1)

  def goToLamanDetail1(self):
      self.channel.emit("page-builder", self.idLaman["laman1"])
  
  def goToLamanDetail2(self):
      self.channel.emit("page-builder", self.idLaman["laman2"])

# if __name__ == "__main__":
#   app = QApplication(sys.argv)
#   window = PermintaanDiterimaWindow()
#   window.show()
#   sys.exit(app.exec())
