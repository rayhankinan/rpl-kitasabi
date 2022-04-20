import sys
import requests
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QRadioButton, QMessageBox, QFileDialog
from PyQt6.QtGui import QFont, QPixmap, QCursor
from PyQt6.QtCore import Qt
from PyQt6.QtCore import pyqtSignal
from requests.auth import HTTPBasicAuth
from views.custom_widgets import ClickableLabel

graybg = '#F2F4F7'
ungu = 'rgba(90, 79, 243, 1)'
white = 'rgba(255, 255, 255, 1)'
tulisan = 'rgba(37, 49, 60, 1)'

class RegisterWindow(QWidget):
  channel = pyqtSignal()

  dataText = {
    "email": "",
    "no-telp": "",
    "nama-depan": "",
    "nama-belakang": "",
    "username": "",
    "password": "",
  }

  dataFile = {
    "foto": ""
  }

  def __init__(self):
    super().__init__()
    self.setUpRegisterWindow()
    # 

  def setUpRegisterWindow(self):
    self.setFixedSize(1440, 1024)
    self.setWindowTitle("KITASABI - Register")
    self.setUpWidgets()

  def setUpWidgets(self):
    # Set warna background
    self.setStyleSheet('''
      QWidget {
        background-color: #E5E5E5;
      }
      QLabel {
        color: #25313C;
        font-weight: extra-bold;
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

    # Heading label
    heading = QLabel(self)
    heading.setText("Daftar")
    heading.setFont(mulish44)
    heading.setStyleSheet(f'color: {tulisan}')
    heading.move(665, 125)

    # Subheading label
    subheading = QLabel(self)
    subheading.setText("Sudah punya akun?")
    subheading.setFont(mulish16)
    subheading.setStyleSheet(f'color: {tulisan}')
    subheading.move(610, 190)

    # Masuk label
    masukDisini = ClickableLabel(self)
    masukDisini.setText("Masuk disini")
    masukDisini.setFont(mulish16)
    masukDisini.setStyleSheet('''
    QLabel {
      color: #5A4FF3; 
      text-decoration: underline; 
    }
    QLabel:hover {
      color: #746bf2;
    }
    ''')
    masukDisini.move(760, 190)
    masukDisini.clicked.connect(self.goToLoginWindow)
    masukDisini.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
    
    # nama depan input
    self.nameDepan = QLineEdit(self)
    self.nameDepan.setPlaceholderText("Nama Depan")
    self.nameDepan.setFixedSize(340, 42)
    self.nameDepan.setFont(mulish16)
    self.nameDepan.move(550, 255)
    self.nameDepan.textChanged.connect(self.setFirstName)
    
    # name Belakang input
    self.nameEdit = QLineEdit(self)
    self.nameEdit.setPlaceholderText("Nama Belakang")
    self.nameEdit.setFixedSize(340, 42)
    self.nameEdit.setFont(mulish16)
    self.nameEdit.move(550, 314)
    self.nameEdit.textChanged.connect(self.setLastName)
    
    # email input
    self.emailEdit = QLineEdit(self)
    self.emailEdit.setPlaceholderText("Email")
    self.emailEdit.setFixedSize(340, 42)
    self.emailEdit.setFont(mulish16)
    self.emailEdit.move(550, 367)
    self.emailEdit.textChanged.connect(self.setEmail)
    
    # No Telepon input
    self.telphoneEdit = QLineEdit(self)
    self.telphoneEdit.setPlaceholderText("Nomor Telepon")
    self.telphoneEdit.setFixedSize(340, 42)
    self.telphoneEdit.setFont(mulish16)
    self.telphoneEdit.move(550, 420)
    self.telphoneEdit.textChanged.connect(self.setTelphone)

    # Username input
    self.unameEdit = QLineEdit(self)
    self.unameEdit.setPlaceholderText("Username")
    self.unameEdit.setFixedSize(340, 42)
    self.unameEdit.setFont(mulish16)
    self.unameEdit.move(550, 473)      
    self.unameEdit.textChanged.connect(self.setUsername)

    # Password input
    self.passwordEdit = QLineEdit(self)
    self.passwordEdit.setPlaceholderText("Password")
    self.passwordEdit.setFixedSize(340, 42)
    self.passwordEdit.setFont(mulish16)
    self.passwordEdit.move(550, 526)
    self.passwordEdit.textChanged.connect(self.setPassword)
    self.passwordEdit.setEchoMode(QLineEdit.EchoMode.Password)

    # Konfirm Password input
    self.confirmPwEdit = QLineEdit(self)
    self.confirmPwEdit.setPlaceholderText("Konfirmasi Password")
    self.confirmPwEdit.setFixedSize(340, 42)
    self.confirmPwEdit.setFont(mulish16)
    self.confirmPwEdit.move(550, 578)
    self.confirmPwEdit.setEchoMode(QLineEdit.EchoMode.Password)

    # Register push button
    self.fotoEdit = QPushButton(self)
    self.fotoEdit.setText("Upload Foto")
    self.fotoEdit.setFixedSize(340, 42)
    self.fotoEdit.setFont(mulish16)
    self.fotoEdit.move(550, 630)
    self.fotoEdit.setStyleSheet('border-radius: 20px')
    self.fotoEdit.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
    self.fotoEdit.clicked.connect(self.uploadFoto)

    # upload foto push button
    self.registerButton = QPushButton(self)
    self.registerButton.setText("Daftar")
    self.registerButton.setFixedSize(183, 43)
    self.registerButton.move(637, 733)
    self.registerButton.setFont(mulish16)
    self.registerButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
    self.registerButton.clicked.connect(self.register)
  
  def goToLoginWindow(self):
    self.channel.emit()

  def sendData(self):
    response = requests.post('http://localhost:3000/akun/register', data=self.dataText, files=self.dataFile)
    if (response.status_code == 201):
      return True
    else:
      return False

  def setFirstName(self):
    self.dataText["nama-depan"] = self.nameDepan.text()

  def setLastName(self):
    self.dataText["nama-belakang"] = self.nameEdit.text()
    
  def setEmail(self):
    self.dataText["email"] = self.emailEdit.text()

  def setTelphone(self):
    self.dataText["no-telp"] = self.telphoneEdit.text()

  def setUsername(self):
    self.dataText["username"] = self.unameEdit.text()
    
  def setPassword(self):
    self.dataText["password"] = self.passwordEdit.text()

  def uploadFoto(self):
    file = QFileDialog.getOpenFileName(self, 'Open a file', '', 'Image (*.jpg*)')
    if file != ('', ''):
        path = file[0]
        self.dataFile["foto"] = open(path, "rb")

  def register(self):
    # # validasi masukan tidak boleh kosong
    if (self.nameEdit.text() == '' or self.unameEdit.text() == '' or self.emailEdit.text() == '' or self.passwordEdit.text() == '' or self.telphoneEdit.text() == '' or self.confirmPwEdit.text() == ''):
      msgBox = QMessageBox()
      msgBox.setText("<p>Please fill out the form properly!</p>")
      msgBox.setWindowTitle("Registration Failed")
      msgBox.setIcon(QMessageBox.Icon.Warning)
      msgBox.setStyleSheet("background-color: white")
      msgBox.setStandardButtons(QMessageBox.StandardButton.Ok)
      msgBox.exec()
      return
    elif (self.passwordEdit.text() != self.confirmPwEdit.text()):
      msgBox = QMessageBox()
      msgBox.setText("<p>Password confirmation does not match password!</p>")
      msgBox.setWindowTitle("Registration Failed")
      msgBox.setIcon(QMessageBox.Icon.Warning)
      msgBox.setStyleSheet("background-color: white")
      msgBox.setStandardButtons(QMessageBox.StandardButton.Ok)
      msgBox.exec()
      return
    success = self.sendData()
    if (success):
      # Tunjukkan registrasi berhasil
      msgBox = QMessageBox()
      msgBox.setText(f"""<p>Welcome to Kitasabi, {self.nameDepan.text()}!</p>
      <p>You will now be prompted to log in.</p>""")
      msgBox.setWindowTitle("Registration Successful")
      msgBox.setIcon(QMessageBox.Icon.Information)
      msgBox.setStyleSheet("background-color: white")
      msgBox.setStandardButtons(QMessageBox.StandardButton.Ok)
      msgBox.exec()
      # Clear form inputs
      self.nameDepan.clear()
      self.nameEdit.clear()
      self.unameEdit.clear()
      self.emailEdit.clear()
      self.passwordEdit.clear()
      self.telphoneEdit.clear()
      self.confirmPwEdit.clear()
      # Emit signal to controller
      self.channel.emit()
    else:
      msgBox = QMessageBox()
      msgBox.setText("<p>Invalid data, try refilling!</p>")
      msgBox.setWindowTitle("Registration Failed")
      msgBox.setIcon(QMessageBox.Icon.Warning)
      msgBox.setStyleSheet("background-color: white")
      msgBox.setStandardButtons(QMessageBox.StandardButton.Ok)
      msgBox.exec()
      return


# if __name__ == "__main__":
#   app = QApplication(sys.argv)
#   window = RegisterWindow()
#   window.show()
#   sys.exit(app.exec())
