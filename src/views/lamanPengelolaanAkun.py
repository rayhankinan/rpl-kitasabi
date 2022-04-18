import sys
from PyQt6.QtWidgets import QApplication, QWidget, QTextEdit, QLabel, QLineEdit, QPushButton, QMessageBox
from PyQt6.QtGui import QFont, QPixmap, QCursor, QImage
from PyQt6.QtCore import Qt
from PyQt6.QtCore import pyqtSignal
from views.custom_widgets import ClickableLabel
import urllib.request

import sys
import urllib.request

graybg = '#F2F4F7'
ungu = 'rgba(90, 79, 243, 1)'
white = 'rgba(255, 255, 255, 1)'
tulisan = 'rgba(37, 49, 60, 1)'

class PengelolaanAkunWindow(QWidget):
  channel = pyqtSignal(str)
  
  def __init__ (self):
    super().__init__()
    self.setUpPengelolaanAkunWindow()
  
  def setUpPengelolaanAkunWindow(self):
    self.setFixedSize(1440, 1024)
    self.setWindowTitle("KITASABI - Laman Pengelolaan Akun")
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
    self.returnButton.setText("< Kembali ke Laman Utama")
    self.returnButton.setFixedSize(258, 36)
    self.returnButton.move(53, 32)
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
    # self.returnButton.clicked.connect(go to laman utama)

    # # profile
    # self.profilePicture = QLabel(self)
    # self.profilePicture.setFixedSize(183,183)
    # self.profilePicture.move(642,42)
    # self.profilePicture.setStyleSheet('''
    #   padding-right: 50px;
    #   padding-top: 25px;
    #   background: #DAE3EA;
    #   border: 20px;
    #   border-radius: 30;
    # ''')
    
    # username label
    self.usernameBg = QLabel(self)
    self.usernameBg.setFixedSize(266, 46)
    self.usernameBg.move(601, 245)
    self.usernameBg.setStyleSheet('background-color: rgba(218, 227, 234, 1)')
    self.usernameLabel = QLabel(self)
    self.usernameLabel.setText("Username")
    self.usernameLabel.move(644, 249)
    self.usernameLabel.setFont(mulish33_bold)
    self.usernameLabel.setStyleSheet('background-color: rgba(218, 227, 234, 1)')
    
    # set bg form
    self.formBg = QLabel(self)
    self.formBg.setFixedSize(1220, 633)
    self.formBg.move(124, 353)
    self.formBg.setStyleSheet('background-color: rgba(187, 200, 212, 1)')

    # nama depan
    self.nameDepanEdit = QLineEdit(self)
    self.nameDepanEdit.setPlaceholderText("Nama Depan")
    self.nameDepanEdit.setDisabled(True)
    self.nameDepanEdit.setFixedSize(580, 63)
    self.nameDepanEdit.setFont(mulish16)
    self.nameDepanEdit.setStyleSheet('''
    padding: 8px 30px 8px 30px;
    border: 2px solid rgba(90, 79, 243, 1);
    color: rgba(37, 49, 60, 1);
    background-color: rgba(218, 227, 234, 1)
    ''')
    self.nameDepanEdit.move(458, 321)
         
    # nama belakang 
    self.nameEdit = QLineEdit(self)
    self.nameEdit.setPlaceholderText("Nama Belakang")
    self.nameEdit.setDisabled(True)
    self.nameEdit.setFixedSize(580, 63)
    self.nameEdit.setFont(mulish16)
    self.nameEdit.setStyleSheet('''
    padding: 8px 30px 8px 30px;
    border: 2px solid rgba(90, 79, 243, 1);
    color: rgba(37, 49, 60, 1);
    background-color: rgba(218, 227, 234, 1)
    ''')
    self.nameEdit.move(458, 406)
    
    # email 
    self.emailEdit = QLineEdit(self)
    self.emailEdit.setPlaceholderText("Email")
    self.emailEdit.setDisabled(True)
    self.emailEdit.setFixedSize(580, 63)
    self.emailEdit.setFont(mulish16)
    self.emailEdit.setStyleSheet('''
    padding: 8px 30px 8px 30px;
    border: 2px solid rgba(90, 79, 243, 1);
    color: rgba(37, 49, 60, 1);
    background-color: rgba(218, 227, 234, 1)
    ''')
    self.emailEdit.move(458, 487)
    
    # no telepon
    self.noTeleponEdit = QLineEdit(self)
    self.noTeleponEdit.setPlaceholderText("No Telepon")
    self.noTeleponEdit.setDisabled(True)
    self.noTeleponEdit.setFixedSize(580, 63)
    self.noTeleponEdit.setFont(mulish16)
    self.noTeleponEdit.setStyleSheet('''
    padding: 8px 30px 8px 30px;
    border: 2px solid rgba(90, 79, 243, 1);
    color: rgba(37, 49, 60, 1);
    background-color: rgba(255, 255, 255, 1)
    ''')
    self.noTeleponEdit.move(458, 565)
    
    # username
    self.usernameEdit = QLineEdit(self)
    self.usernameEdit.setFixedSize(580, 63)
    self.usernameEdit.setPlaceholderText("Username")
    self.usernameEdit.setFont(mulish16)
    self.usernameEdit.setStyleSheet('''
    padding: 8px 30px 8px 30px;
    border: 2px solid rgba(90, 79, 243, 1);
    color: rgba(37, 49, 60, 1);
    background-color: rgba(255, 255, 255, 1)
    ''')
    self.usernameEdit.move(458, 645)
    
    # password
    self.passwordEdit = QLineEdit(self)
    self.passwordEdit.setFixedSize(580, 63)
    self.passwordEdit.setPlaceholderText("Password")
    self.passwordEdit.setFont(mulish16)
    self.passwordEdit.setStyleSheet('''
    padding: 8px 30px 8px 30px;
    border: 2px solid rgba(90, 79, 243, 1);
    color: rgba(37, 49, 60, 1);
    background-color: rgba(255, 255, 255, 1)
    ''')
    self.passwordEdit.move(458, 725)

    # konfirmasi password
    self.confirmPassword = QLineEdit(self)
    self.confirmPassword.setFixedSize(580, 63)
    self.confirmPassword.setPlaceholderText("Konfirmasi Password")
    self.confirmPassword.setFont(mulish16)
    self.confirmPassword.setStyleSheet('''
    padding: 8px 30px 8px 30px;
    border: 2px solid rgba(90, 79, 243, 1);
    color: rgba(37, 49, 60, 1);
    background-color: rgba(255, 255, 255, 1)
    ''')
    self.confirmPassword.move(458, 803)
    
    # perbarui button
    self.perbaruiButton = QPushButton(self)
    self.perbaruiButton.setText("Perbarui")
    self.perbaruiButton.setFixedSize(165, 56)
    self.perbaruiButton.move(664, 906)
    self.perbaruiButton.setStyleSheet('''
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
    self.perbaruiButton.setFont(mulish24)
    self.perbaruiButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
    # perbarui data
    self.perbaruiButton.clicked.connect(self.register)
  
  def register(self):
    # register 
    self.goToMainWindow()
  
  def goToMainWindow(self):
    self.channel.emit("mainWindow")

# if __name__ == "__main__":
#   app = QApplication(sys.argv)
#   window = PengelolaanAkunWindow()
#   window.show()
#   sys.exit(app.exec())
