import sys
import PyQt6 
from PyQt6.QtWidgets import QApplication
from views.lamanPembayaran import LamanPembayaran
from views.formLogin import LoginWindow
from views.formRegister import RegisterWindow
from views.lamanDetail import LamanDetail
from views.lamanEksplor import LamanEksplor
from views.formKesehatan import FormKesehatan
from views.formNonKesehatan import FormNonKesehatan
from views.lamanPengelolaanAkun import PengelolaanAkunWindow
from views.lamanPenggalangDana import LamanPenggalangDana
from views.lamanRiwayatDonasi import RiwayatDonasiWindow
from views.lamanRiwayatPenggalanganDana import RiwayatPenggalanganWindow
from views.lamanPermintaan import LamanPermintaan
from views.mainWindow import MainWindow
from views.pageBuilder import PageBuilder


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
		self.lamanPermintaan = LamanPermintaan()
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
		self.lamanPermintaan.channel.connect(self.handleLamanPermintaan)
		self.lamanPengelolaanAkun.channel.connect(self.handleLamanPengelolaanAkun)

	def handleLamanPembayaran(self, nextPage):
		if (nextPage == "home"):
			self.mainWindow.setLaman()
			self.lamanPembayaran.close()
			self.mainWindow.show()
		elif (nextPage == "profile"):
			self.lamanPembayaran.close()
			self.lamanPengelolaanAkun.show()
		else:
			self.lamanRiwayatDonasi.setLaman()
			self.lamanPembayaran.close()
			self.lamanRiwayatDonasi.show()

	def handleLamanDetail(self, nextPage, idLaman):
		if (nextPage == "home"):
			self.mainWindow.setLaman()
			self.lamanDetail.close()
			self.mainWindow.show()
		elif (nextPage == "profile"):
			self.lamanDetail.close()
			self.lamanPengelolaanAkun.show()
		else:
			self.lamanPembayaran.setLaman(idLaman)
			self.lamanDetail.close()
			self.lamanPembayaran.show()

	def handleLamanEksplor(self, nextPage, idLaman):
		if (nextPage == "home"):
			self.mainWindow.setLaman()
			self.lamanEksplor.close()
			self.mainWindow.show()
		elif (nextPage == "profile"):
			self.lamanEksplor.close()
			self.lamanPengelolaanAkun.show()
		else:
			self.lamanDetail.setLaman(idLaman)
			self.lamanEksplor.close()
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
		self.lamanPermintaan.setLaman()
		self.pageBuilder.close()
		self.lamanPermintaan.show()

	def handleFormLogin(self, nextPage, usernameEmail, password):
		if (nextPage == "register"):
			self.formLogin.close()
			self.formRegister.show()
		elif(nextPage == "mainWindow"):
			self.formKesehatan.setSession(usernameEmail, password)
			self.formNonKesehatan.setSession(usernameEmail, password)
			self.lamanDetail.setSession(usernameEmail, password)
			self.lamanEksplor.setSession(usernameEmail, password)
			self.lamanPembayaran.setSession(usernameEmail, password)
			self.lamanPermintaan.setSession(usernameEmail, password)
			self.mainWindow.setSession(usernameEmail, password)
			self.pageBuilder.setSession(usernameEmail, password)
			self.lamanRiwayatPenggalanganDana.setSession(usernameEmail, password)
			self.lamanRiwayatDonasi.setSession(usernameEmail, password)
			self.lamanPermintaan.setSession(usernameEmail, password)
			self.lamanPengelolaanAkun.setSession(usernameEmail, password)
			self.mainWindow.setLaman()
			self.formLogin.close()
			self.mainWindow.show()
	
	def handleFormRegister(self):
		self.formRegister.close()
		self.formLogin.show()

	def handleMainWindow(self, nextPage, idLaman):
		if (nextPage == "riwayat_penggalangan_dana"):
			self.lamanRiwayatPenggalanganDana.setLaman()
			self.mainWindow.close()
			self.lamanRiwayatPenggalanganDana.show()
		elif (nextPage == "lihat_detail"):
			self.lamanDetail.setLaman(idLaman)
			self.mainWindow.close()
			self.lamanDetail.show()
		elif (nextPage == "pengelolaan_akun"):
			self.mainWindow.close()
			self.lamanPengelolaanAkun.show()
		elif (nextPage == "mulai_penggalang"):
			self.mainWindow.close()
			self.lamanPenggalangDana.show()
		elif (nextPage == "riwayat_donasi"):
			self.lamanRiwayatDonasi.setLaman()
			self.mainWindow.close()
			self.lamanRiwayatDonasi.show()
		elif (nextPage == "riwayat_penggalangan_dana"):
			self.lamanRiwayatPenggalanganDana.setLaman()
			self.mainWindow.close()
			self.lamanRiwayatPenggalanganDana.show()
		elif (nextPage == "eksplor"):
			self.lamanEksplor.setLaman()
			self.mainWindow.close()
			self.lamanEksplor.show()
		elif (nextPage == "permintaan"):
			self.lamanPermintaan.setLaman()
			self.mainWindow.close()
			self.lamanPermintaan.show()
		else:
			pass
		
	def handleLamanRiwayatDonasi(self):
		self.mainWindow.setLaman()
		self.lamanRiwayatDonasi.close()
		self.mainWindow.show()

	def handleLamanRiwayatPenggalanganDana(self, nextPage):
		if (nextPage == "utama"):
			self.mainWindow.setLaman()
			self.lamanRiwayatPenggalanganDana.close()
			self.mainWindow.show()
		else:
			self.lamanRiwayatPenggalanganDana.close()
			self.lamanPenggalangDana.show()
			
	
	def handleLamanPengelolaanAkun(self, nextPage):
		self.mainWindow.setLaman()
		self.lamanPengelolaanAkun.close()
		self.mainWindow.show()

	def handleLamanPermintaan(self, nextPage, idLaman):
		if (nextPage == "page-builder"):
			self.pageBuilder.setLaman(idLaman)
			self.lamanPermintaan.close()
			self.pageBuilder.show()
		elif (nextPage == "profile"):
			self.lamanPermintaan.close()
			self.lamanPengelolaanAkun.show()
		else:
			self.lamanPermintaan.close()
			self.mainWindow.show()

	
# if __name__ == "__main__":
#   app = QApplication(sys.argv)
#   window = PageController()
# #   window.show()
#   sys.exit(app.exec())
