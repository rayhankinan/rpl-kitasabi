import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QMessageBox
from PyQt6.QtGui import QFont, QCursor
from PyQt6.QtCore import Qt
from PyQt6.QtCore import pyqtSignal
from custom_widgets import ClickableLabel

class LoginWindow(QWidget):
  channel = pyqtSignal(str)

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
    self.setStyleSheet('background-color: #E5E5E5')

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
    loginText.setStyleSheet('''
      color: #25313C;
      background-color: #E5E5E5
      font-weight: extra-bold;
    ''')
    loginText.move(700, 275)
    loginText.setFont(mulish44)

    # Input username/email
    self.usernameEdit = QLineEdit(self)
    self.usernameEdit.setPlaceholderText("Email atau Username")
    self.usernameEdit.setFixedSize(446, 46)
    self.usernameEdit.move(560, 456)
    self.usernameEdit.setStyleSheet('''
      padding: 11px 30px 11px 30px;
      border: 2px solid rgba(90, 79, 243, 1);
      border-radius: 20px;
      color: rgba(37, 49, 60, 1);
      background-color: #FFFFFF
    ''')
    self.usernameEdit.setFont(mulish16)

    # Input password
    self.passwordEdit = QLineEdit(self)
    self.passwordEdit.setPlaceholderText("Password")
    self.passwordEdit.setFixedSize(446, 46)
    self.passwordEdit.move(560, 528)
    self.passwordEdit.setStyleSheet('''
      padding: 11px 30px 11px 30px;
      border: 2px solid rgba(90, 79, 243, 1);
      border-radius: 20px;
      color: rgba(37, 49, 60, 1);
      background-color: #FFFFFF
    ''')
    self.passwordEdit.setFont(mulish16)
    self.passwordEdit.setEchoMode(QLineEdit.EchoMode.Password)

    # Log in push button
    self.loginButton = QPushButton(self)
    self.loginButton.setText("Masuk")
    self.loginButton.setFixedSize(170, 56)
    self.loginButton.move(680, 637)
    self.loginButton.setStyleSheet('''
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
    self.loginButton.setFont(mulish16)
    self.loginButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
    self.loginButton.clicked.connect(self.login)

    # Don't have an account? label
    label = QLabel(self)
    label.setText("Belum Punya Akun?")
    label.setFont(mulish24)
    label.setStyleSheet('color: rgba(0, 0, 0, 1)')
    label.move(600, 350)

    # Register here label
    registerHere = ClickableLabel(self)
    registerHere.setText("Daftar disini")
    registerHere.setFont(mulish24)
    registerHere.setStyleSheet('''
      QLabel {
        color: #5A4FF3; 
        text-decoration: underline; 
      }
      QLabel:hover {
        color: #746bf2;
      }
    '''
    )
    registerHere.move(810, 350)
    registerHere.clicked.connect(self.goToRegisterWindow)
    registerHere.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

  def goToRegisterWindow(self):
    self.channel.emit("register")
  
  def goToMainWindow(self):
    self.channel.emit("mainWindow")

  def login(self):
    # fetch
    self.clearForm()
    self.goToMainWindow()
              
  def clearForm(self):
    self.passwordEdit.clear()
    self.usernameEdit.clear()

# if __name__ == "__main__":
#   # app = QApplication(sys.argv)
#   # window = LoginWindow()
#   # window.show()
#   # sys.exit(app.exec())