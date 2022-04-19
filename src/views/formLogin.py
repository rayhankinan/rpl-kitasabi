import sys
import requests
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QMessageBox
from PyQt6.QtGui import QFont, QCursor
from PyQt6.QtCore import Qt
from PyQt6.QtCore import pyqtSignal
from views.custom_widgets import ClickableLabel

class LoginWindow(QWidget):
  channel = pyqtSignal(str)

  dataText = {
    "email-username": "",
    "password": "",
  }

  def __init__(self):
    super().__init__()
    self.setUpLoginWindow()
    # connect ke database
    # self.conn

  def setUpLoginWindow(self):
    self.setFixedSize(1440, 1024)
    self.setWindowTitle("KITASABI - Log In")
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

    # Label log in
    loginText = QLabel(self)
    loginText.setText("Masuk")
    loginText.move(700, 225)
    loginText.setFont(mulish44)

    # Input username/email
    self.usernameEdit = QLineEdit(self)
    self.usernameEdit.setPlaceholderText("Email atau Username")
    self.usernameEdit.setFixedSize(446, 46)
    self.usernameEdit.move(540, 356)
    self.usernameEdit.setFont(mulish16)
    self.usernameEdit.textChanged.connect(self.setUsername)

    # Input password
    self.passwordEdit = QLineEdit(self)
    self.passwordEdit.setPlaceholderText("Password")
    self.passwordEdit.setFixedSize(446, 46)
    self.passwordEdit.move(540, 428)
    self.passwordEdit.setFont(mulish16)
    self.passwordEdit.setEchoMode(QLineEdit.EchoMode.Password)
    self.passwordEdit.textChanged.connect(self.setPassword)

    # Log in push button
    self.loginButton = QPushButton(self)
    self.loginButton.setText("Masuk")
    self.loginButton.setFixedSize(170, 56)
    self.loginButton.move(680, 537)
    self.loginButton.setFont(mulish16)
    self.loginButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
    self.loginButton.clicked.connect(self.login)

    # Don't have an account? label
    label = QLabel(self)
    label.setText("Belum Punya Akun?")
    label.setFont(mulish16)
    label.setStyleSheet('color: rgba(0, 0, 0, 1)')
    label.move(650, 290)

    # Register here label
    registerHere = ClickableLabel(self)
    registerHere.setText("Daftar disini")
    registerHere.setFont(mulish16)
    registerHere.setStyleSheet('''
      QLabel {
        color: #5A4FF3; 
        text-decoration: underline; 
      }
      QLabel:hover {
        color: #746bf2;
      }
    ''')
    registerHere.move(800, 290)
    registerHere.clicked.connect(self.goToRegisterWindow)
    registerHere.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

  def setPassword(self):
    self.dataText["password"] = self.passwordEdit.text()
  def setUsername(self):
    self.dataText["email-username"] = self.usernameEdit.text()

  def goToRegisterWindow(self):
    self.channel.emit("register")
  
  def goToMainWindow(self):
    self.channel.emit("mainWindow")

  def sendData(self):
    response = requests.post('http://localhost:3000/akun/login', data=self.dataText)
    if (response.status_code == 201):
      return True
    else:
      return False

  def login(self):
    for key, value in self.dataText.items():
      if (value == ""):
        print(key + value)
        msgBox = QMessageBox()
        msgBox.setText("<p>Please fill out the form properly!</p>")
        msgBox.setWindowTitle("Login Failed")
        msgBox.setIcon(QMessageBox.Icon.Warning)
        msgBox.setStyleSheet("background-color: white")
        msgBox.setStandardButtons(QMessageBox.StandardButton.Ok)
        msgBox.exec()
        return
    success = self.sendData()
    if (success):
      # fetch
      self.resetState()
      self.goToMainWindow()
      for key in self.dataText.items():
        self.dataText[key] = ""
    else:
      print(key + value)
      msgBox = QMessageBox()
      msgBox.setText("<p>Account not registered, register first!</p>")
      msgBox.setWindowTitle("Login Failed")
      msgBox.setIcon(QMessageBox.Icon.Warning)
      msgBox.setStyleSheet("background-color: white")
      msgBox.setStandardButtons(QMessageBox.StandardButton.Ok)
      msgBox.exec()
      return
              
  def resetState(self):
    self.passwordEdit.clear()
    self.usernameEdit.clear()

# if __name__ == "__main__":
#   # app = QApplication(sys.argv)
#   # window = LoginWindow()
#   # window.show()
#   # sys.exit(app.exec())
