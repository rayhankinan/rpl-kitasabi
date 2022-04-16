from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QTextEdit, QPushButton, QFileDialog, QCalendarWidget, QHBoxLayout
from PyQt6.QtGui import QFont, QCursor
from PyQt6.QtCore import Qt, QDate
import sys

class PageBuilder(QWidget):
    def __init__(self):
        super().__init__()
        
        # set overall page layout
        self.setFixedSize(1440, 1024)
        self.setWindowTitle("KITASABI - Page Builder")
        self.setStyleSheet('background-color: #F2F4F7')

        # nanti janlup connect database

        # set fonts
        mulish16 = QFont()
        mulish16.setFamily("Mulish"); mulish16.setPixelSize(16)
        mulish24 = QFont()
        mulish24.setFamily("Mulish"); mulish24.setPixelSize(24)
        mulish44 = QFont()
        mulish44.setFamily("Mulish"); mulish44.setPixelSize(44)
        self.setWidget()
        
    def setWidget(self):
        # set page title label
        text = QLabel(self)
        text.setText("Pembuatan Laman Penggalangan Dana")
        text.setStyleSheet('''
            color: #25313C;
            font-weight: 700;
            font-size: 36px;
            line-height: 24px;
        ''')
        text.move(374, 93)

        # set fixed judul box
        self.judulFixed = QTextEdit(self)
        self.judulFixed.setEnabled(False)
        self.judulFixed.setPlaceholderText("tolong keluarga ini membeli beras (ISI PAKE DATA DR DATABASE)")
        self.judulFixed.setFixedSize(377, 47)
        self.judulFixed.move(531, 208)
        self.judulFixed.setStyleSheet('''
            border: 2px solid #5A4FF3;
            background-color: #DAE3EA;
            padding: 10px 10px 10px 10px;
        ''')

        # set upload foto box
        self.uploadFoto = QPushButton(self)
        self.uploadFoto.setText("Upload Foto")
        self.uploadFoto.setFixedSize(377, 47)
        self.uploadFoto.move(531, 274)
        self.uploadFoto.setStyleSheet('''
            QPushButton {
                border: 2px solid #5A4FF3;
                background-color: #FFFFFF;
                padding: 10px 10px 10px 10px;
            }
            QPushButton:hover {
                background-color: #5A4FF3
            }
        ''')
        self.uploadFoto.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.uploadFoto.clicked.connect(self.openFile)

        # set fixed deskripsi box
        self.descFixed = QTextEdit(self)
        self.descFixed.setEnabled(False)
        self.descFixed.setPlaceholderText("ibu jubaidah dan anaknya ilham ingin membeli beras tolonglah mereka membeli segelintir beras (ISI PAKE DATA DR DATABASE)")
        self.descFixed.setFixedSize(377, 163)
        self.descFixed.move(531, 339)
        self.descFixed.setStyleSheet('''
            border: 2px solid #5A4FF3;
            background-color: #DAE3EA;
            padding: 10px 10px 10px 10px;
        ''')

        # set fixed target donasi box
        self.targetFixed = QTextEdit(self)
        self.targetFixed.setEnabled(False)
        self.targetFixed.setPlaceholderText("10 juta (ISI PAKE DATA DR DATABASE)")
        self.targetFixed.setFixedSize(377, 47)
        self.targetFixed.move(531, 521)
        self.targetFixed.setStyleSheet('''
            border: 2px solid #5A4FF3;
            background-color: #DAE3EA;
            padding: 10px 10px 10px 10px;
        ''')

        # set date picker box
        self.setDeadline = QPushButton(self)
        self.setDeadline.setText("Pilih Tenggat Waktu")
        self.setDeadline.setFixedSize(377, 47)
        self.setDeadline.move(531, 586)
        self.setDeadline.setStyleSheet('''
            QPushButton {
                border: 2px solid #5A4FF3;
                background-color: #FFFFFF;
                padding: 10px 10px 10px 10px;
            }
            QPushButton:hover {
                background-color: #5A4FF3
            }
        ''')
        self.setDeadline.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.setDeadline.clicked.connect(self.pickDate)

        # set submit button
        self.submitPage = QPushButton(self)
        self.submitPage.setText("SUBMIT")
        self.submitPage.setFixedSize(165, 52)
        self.submitPage.move(638, 664)
        self.submitPage.setStyleSheet('''
            QPushButton {
                border: 2px solid #5A4FF3;
                border-radius: 20px;
                background-color: #5A4FF3;
                padding: 10px 10px 10px 10px;
            }
            QPushButton:hover {
                background-color: #FFFFFF;
            }
        ''')
        self.submitPage.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        # self.submitPage.clicked.connect(send)

    # get jpg file
    def openFile(self):
        file = QFileDialog.getOpenFileName(self, 'Open a file', '', 'Image (*.jpg*)')
        if file != ('', ''):
            path = file[0]
            print(path)
            # TEST OPEN TXT FILE
            # with open(path, "r") as f:
            #     print(f.readline())
            
    # get date
    def pickDate(self):
        # date picker
        self.cal = QCalendarWidget(self)
        self.cal.setGridVisible(True)
        self.cal.clicked[QDate].connect(self.setDate)
        
        # pop up calendar view
        self.calendarWindow = QWidget()
        viewbox = QHBoxLayout()
        viewbox.addWidget(self.cal)
        self.calendarWindow.setLayout(viewbox)
        self.calendarWindow.setGeometry(300, 300, 415, 350)
        self.calendarWindow.setWindowTitle('Pilih Tanggal')
        self.calendarWindow.show()

    # set input as selected date
    def setDate(self, date):
        self.setDeadline.setText(date.toString())


# UNCOMMENT BELOW FOR TESTING  
app = QApplication(sys.argv)
window = PageBuilder()
window.show()
sys.exit(app.exec())
