import sys
import PyQt6 
from PyQt6.QtWidgets import QApplication
from lamanPembayaran import LamanPembayaran
from formLogin import LoginWindow
from formRegister import RegisterWindow
from lamanDetail import LamanDetail
from lamanEksplor import LamanEksplor
from formKesehatan import FormKesehatan
from formNonKesehatan import FormNonKesehatan
from lamanPengelolaanAkun import PengelolaanAkunWindow
from lamanPenggalangDana import LamanPenggalangDana
from lamanRiwayatDonasi import RiwayatDonasiWindow
from lamanRiwayatPenggalanganDana import RiwayatPenggalanganWindow
from mainWindow import MainWindow
from pageBuilder import PageBuilder


class PageController:
	def __init__ (self):
		super().__init__()
		self.setUpPages()
		self.setListener()
		self.formLogin.show()

	def setUpPages(self):
		self.lamanPembayaran = LamanPembayaran()
		self.formKesehatan = FormKesehatan()
		self.formNonKesehatan = FormNonKesehatan()
		self.formLogin = LoginWindow()
		self.formRegister = RegisterWindow()
		self.lamanDetail = LamanDetail()
		self.lamanEksplor = LamanEksplor()
		self.lamanPengelolaanAkun = PengelolaanAkunWindow()
		self.lamanPenggalangDana = LamanPenggalangDana()
		self.lamanRiwayatDonasi = RiwayatDonasiWindow()
		self.lamanRiwayatPenggalanganDana = RiwayatPenggalanganWindow()
		self.mainWindow = MainWindow()
		self.pageBuilder = PageBuilder()

	def setListener(self):
		self.lamanPembayaran.channel.connect(self.handleLamanPembayaran)
		self.lamanDetail.channel.connect(self.handleLamanDetail)
		self.lamanEksplor.channel.connect(self.handleLamanEksplor)
		self.lamanPenggalangDana.channel.connect(self.handleLamanPenggalangDana)
		self.formKesehatan.channel.connect(self.handleFormKesehatan)
		self.formNonKesehatan.channel.connect(self.handleFormNonKesehatan)
		self.pageBuilder.channel.connect(self.handlePageBuilder)
		self.mainWindow.channel.connect(self.handleMainWindow)
		self.formLogin.channel.connect(self.handleFormLogin)
		self.formRegister.channel.connect(self.handleFormRegister)
		self.lamanRiwayatDonasi.channel.connect(self.handleLamanRiwayatDonasi)
		self.lamanRiwayatPenggalanganDana.channel.connect(self.handleLamanRiwayatPenggalanganDana)

		self.lamanPengelolaanAkun.channel.connect(self.handleLamanPengelolaanAkun)

	def handleLamanPembayaran(self, nextPage):
		self.lamanPembayaran.close()
		if (nextPage == "home"):
			self.mainWindow.show()
		elif (nextPage == "profile"):
			self.lamanPengelolaanAkun.show()
		else:
			self.lamanRiwayatPenggalanganDana.show()

	def handleLamanDetail(self, nextPage):
		self.lamanDetail.close()
		if (nextPage == "home"):
			self.mainWindow.show()
		elif (nextPage == "profile"):
			self.lamanPengelolaanAkun.show()
		else:
			self.lamanPembayaran.show()

	def handleLamanEksplor(self, nextPage):
		self.lamanEksplor.close()
		if (nextPage == "home"):
			self.mainWindow.show()
		elif (nextPage == "profile"):
			self.lamanPengelolaanAkun.show()
		else:
			self.lamanDetail.show()

	def handleLamanPenggalangDana(self, nextPage):
		self.lamanPenggalangDana.close()
		if (nextPage == "kesehatan"):
			self.formKesehatan.show()
		else:
			self.formNonKesehatan.show()

	def handleFormKesehatan(self):
		self.formKesehatan.close()
		self.lamanRiwayatPenggalanganDana.show()
	
	def handleFormNonKesehatan(self):
		self.formNonKesehatan.close()
		self.lamanRiwayatPenggalanganDana.show()

	def handlePageBuilder(self):
		self.pageBuilder.close()
		self.lamanPenggalangDana.show()

	def handleFormLogin(self, nextPage):
		self.formLogin.close()
		if (nextPage == "register"):
			self.formRegister.show()
		elif(nextPage == "mainWindow"):
			self.mainWindow.show()
	
	def handleFormRegister(self):
		self.formRegister.close()
		self.formLogin.show()

	def handleMainWindow(self, nextPage):
		self.mainWindow.close()
		if (nextPage == "riwayat_penggalangan_dana"):
			self.lamanRiwayatPenggalanganDana.show()
		elif (nextPage == "lihat_detail"):
			self.lamanDetail.show()
		elif (nextPage == "pengelolaan_akun"):
			self.lamanPengelolaanAkun.show()
		elif (nextPage == "mulai_penggalang"):
			self.lamanPenggalangDana.show()
		elif (nextPage == "riwayat_donasi"):
			self.lamanRiwayatDonasi.show()
		elif (nextPage == "riwayat_penggalangan_dana"):
			self.lamanRiwayatPenggalanganDana.show()
		elif (nextPage == "eksplor"):
			self.lamanEksplor.show()
		elif (nextPage == "permintaan"):
			pass
		else:
			pass
		
	def handleLamanRiwayatDonasi(self):
		self.lamanRiwayatDonasi.close()
		self.lamanEksplor.show()

	def handleLamanRiwayatPenggalanganDana(self, nextPage):
		self.lamanRiwayatDonasi.close()
		if (nextPage == "eksplor"):
			self.lamanEksplor.show()
		else:
			self.lamanPenggalangDana.show()
			
	
	def handleLamanPengelolaanAkun(self, nextPage):
		self.lamanPengelolaanAkun.close()
		if (nextPage == "mainWindow"):
			self.mainWindow.show()

if __name__ == "__main__":
  app = QApplication(sys.argv)
  window = PageController()
#   window.show()
  sys.exit(app.exec())