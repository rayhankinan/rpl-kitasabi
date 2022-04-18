import sys
import requests
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QRadioButton, QMessageBox
from PyQt6.QtGui import QFont, QPixmap, QCursor
from PyQt6.QtCore import Qt
from PyQt6.QtCore import pyqtSignal
from custom_widgets import ClickableLabel

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
    self.setStyleSheet('background-color: {graybg};')

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
    heading.move(638, 212)

    # Subheading label
    subheading = QLabel(self)
    subheading.setText("Sudah punya akun?")
    subheading.setFont(mulish24)
    subheading.setStyleSheet(f'color: {tulisan}')
    subheading.move(561, 273)

    # Masuk label
    masukDisini = ClickableLabel(self)
    masukDisini.setText("Masuk disini")
    masukDisini.setFont(mulish24)
    masukDisini.setStyleSheet('''
    QLabel {
      color: #5A4FF3; 
      text-decoration: underline; 
    }
    QLabel:hover {
      color: #746bf2;
    }
    '''
    )
    masukDisini.move(770, 273)
    masukDisini.clicked.connect(self.goToLoginWindow)
    masukDisini.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
    
    # nama depan input
    self.nameDepan = QLineEdit(self)
    self.nameDepan.setPlaceholderText("Nama Depan")
    self.nameDepan.setFixedSize(340, 42)
    self.nameDepan.setFont(mulish16)
    self.nameDepan.setStyleSheet('''
    padding: 8px 30px 8px 30px;
    border: 2px solid rgba(90, 79, 243, 1);
    color: rgba(37, 49, 60, 1);
    background-color: rgba(255, 255, 255, 1)
    ''')
    self.nameDepan.move(550, 325)
    self.nameDepan.textChanged.connect(self.setFirsttName)
    
    # name Belakang input
    self.nameEdit = QLineEdit(self)
    self.nameEdit.setPlaceholderText("Nama Belakang")
    self.nameEdit.setFixedSize(340, 42)
    self.nameEdit.setFont(mulish16)
    self.nameEdit.setStyleSheet('''
    padding: 8px 30px 8px 30px;
    border: 2px solid rgba(90, 79, 243, 1);
    color: rgba(37, 49, 60, 1);
    background-color: rgba(255, 255, 255, 1)
    ''')
    self.nameEdit.move(550, 384)
    self.nameEdit.textChanged.connect(self.setLastName)
    
    # email input
    self.emailEdit = QLineEdit(self)
    self.emailEdit.setPlaceholderText("Email")
    self.emailEdit.setFixedSize(340, 42)
    self.emailEdit.setFont(mulish16)
    self.emailEdit.setStyleSheet('''
    padding: 8px 30px 8px 30px;
    border: 2px solid rgba(90, 79, 243, 1);
    color: rgba(37, 49, 60, 1);
    background-color: rgba(255, 255, 255, 1)
    ''')
    self.emailEdit.move(550, 437)
    self.emailEdit.textChanged.connect(self.setEmail)
    
    # No Telepon input
    self.telphoneEdit = QLineEdit(self)
    self.telphoneEdit.setPlaceholderText("Nomor Telepon")
    self.telphoneEdit.setFixedSize(340, 42)
    self.telphoneEdit.setFont(mulish16)
    self.telphoneEdit.setStyleSheet('''
    padding: 8px 30px 8px 30px;
    border: 2px solid rgba(90, 79, 243, 1);
    color: rgba(37, 49, 60, 1);
    background-color: rgba(255, 255, 255, 1)
    ''')
    self.telphoneEdit.move(550, 490)
    self.telphoneEdit.textChanged.connect(self.setTelphone)

    # Username input
    self.unameEdit = QLineEdit(self)
    self.unameEdit.setPlaceholderText("Username")
    self.unameEdit.setFixedSize(340, 42)
    self.unameEdit.setFont(mulish16)
    self.unameEdit.setStyleSheet('''
    padding: 8px 30px 8px 30px;
    border: 2px solid rgba(90, 79, 243, 1);
    color: rgba(37, 49, 60, 1);
    background-color: rgba(255, 255, 255, 1)
    ''')
    self.unameEdit.move(550, 543)      
    self.unameEdit.textChanged.connect(self.setUsername)

    # Password input
    self.passwordEdit = QLineEdit(self)
    self.passwordEdit.setPlaceholderText("Password")
    self.passwordEdit.setFixedSize(340, 42)
    self.passwordEdit.setFont(mulish16)
    self.passwordEdit.setStyleSheet('''
    padding: 8px 30px 8px 30px;
    border: 2px solid rgba(90, 79, 243, 1);
    color: rgba(37, 49, 60, 1);
    background-color: rgba(255, 255, 255, 1)
    ''')
    self.passwordEdit.move(550, 596)
    self.passwordEdit.textChanged.connect(self.setPassword)
    

    # Konfirm Password input
    self.confirmPwEdit = QLineEdit(self)
    self.confirmPwEdit.setPlaceholderText("Konfirmasi Password")
    self.confirmPwEdit.setFixedSize(340, 42)
    self.confirmPwEdit.setFont(mulish16)
    self.confirmPwEdit.setStyleSheet('''
    padding: 8px 30px 8px 30px;
    border: 2px solid rgba(90, 79, 243, 1);
    color: rgba(37, 49, 60, 1);
    background-color: rgba(255, 255, 255, 1)
    ''')
    self.confirmPwEdit.move(550, 648)
    # Register push button
    self.registerButton = QPushButton(self)
    self.registerButton.setText("Daftar")
    self.registerButton.setFixedSize(183, 48)
    self.registerButton.move(637, 753)
    self.registerButton.setStyleSheet('''
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
    self.registerButton.setFont(mulish24)
    self.registerButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
    self.registerButton.clicked.connect(self.register)
  
  def goToLoginWindow(self):
    self.channel.emit()

  def sendData(self):
    response = requests.post('http://localhost:3000/akun/register', data=self.dataText, files=self.dataFile)
    if (response.status_code == 201):
      print("BERHASIL")
    else:
      print("GAGAL")

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

  def register(self):
    # # validasi masukan tidak boleh kosong
    # if (self.nameEdit.text() == '' or self.unameEdit.text() == '' or self.emailEdit.text() == '' or self.passwordEdit.text() == '' or self.telphoneEdit.text() == '' or self.confirmPwEdit.text() == ''):
    #     msgBox = QMessageBox()
    #     msgBox.setText("<p>Please fill out the form properly!</p>")
    #     msgBox.setWindowTitle("Registration Failed")
    #     msgBox.setIcon(QMessageBox.Icon.Warning)
    #     msgBox.setStyleSheet("background-color: white")
    #     msgBox.setStandardButtons(QMessageBox.StandardButton.Ok)
    #     msgBox.exec()
    #     return
    # # validasi username tidak boleh yg sudah terdaftar
    # if (c.fetchone() != None):
    #   msgBox = QMessageBox()
    #   msgBox.setText("<p>Username Sudah Terdaftar!</p>")
    #   msgBox.setWindowTitle("Registrasi Gagal!")
    #   msgBox.setIcon(QMessageBox.Icon.Warning)
    #   msgBox.setStyleSheet("background-color: white")
    #   msgBox.setStandardButtons(QMessageBox.StandardButton.Ok)
    #   msgBox.exec()
    #   return
    # c.execute(f"SELECT * FROM user WHERE email = '{self.emailEdit.text()}'")
    # # validasi email tidak boleh yang sudah terdaftar
    # if (c.fetchone() != None):
    #   msgBox = QMessageBox()
    #   msgBox.setText("<p>Email sudah terdaftar!</p>")
    #   msgBox.setWindowTitle("Registrasi Gagal!")
    #   msgBox.setIcon(QMessageBox.Icon.Warning)
    #   msgBox.setStyleSheet("background-color: white")
    #   msgBox.setStandardButtons(QMessageBox.StandardButton.Ok)
    #   msgBox.exec()
    #   return  
    # c.execute(f"SELECT * FROM user WHERE telephone = '{self.telphoneEdit.text()}'")
    # # validasi telephone tidak boleh yang sudah terdaftar
    # if (c.fetchone() != None):
    #   msgBox = QMessageBox()
    #   msgBox.setText("<p>Telephone sudah terdaftar!</p>")
    #   msgBox.setWindowTitle("Registrasi Gagal!")
    #   msgBox.setIcon(QMessageBox.Icon.Warning)
    #   msgBox.setStyleSheet("background-color: white")
    #   msgBox.setStandardButtons(QMessageBox.StandardButton.Ok)
    #   msgBox.exec()
    #   return
    # # validasi konfirmasi password
    # if (self.passwordEdit.text() != self.confirmPwEdit.text()):
    #   msgBox = QMessageBox()
    #   msgBox.setText("<p>Konfirmasi Password TIdak Sesuai!</p>")
    #   msgBox.setWindowTitle("Registrasi Gagal!")
    #   msgBox.setIcon(QMessageBox.Icon.Warning)
    #   msgBox.setStyleSheet("background-color: white")
    #   msgBox.setStandardButtons(QMessageBox.StandardButton.Ok)
    #   msgBox.exec()
    #   return 
    # jika memenuhi syarat maka register, ini masih salah nanti edit lagi
    self.sendData()
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


if __name__ == "__main__":
  app = QApplication(sys.argv)
  window = RegisterWindow()
  window.show()
  sys.exit(app.exec())
