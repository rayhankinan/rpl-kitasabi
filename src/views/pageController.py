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
from views.lamanPermintaanDiterima import PermintaanDiterimaWindow
from views.mainWindow import MainWindow
from views.pageBuilder import PageBuilder
from views.lamanPermintaanPending import PermintaanPendingWindow


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
		self.lamanPermintaanDiterima = PermintaanDiterimaWindow()
		self.mainWindow = MainWindow()
		self.pageBuilder = PageBuilder()
		self.lamanPermintaanPending = PermintaanPendingWindow()

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
		self.lamanPermintaanDiterima.channel.connect(self.handleLamanPermintaanDiterima)
		self.lamanPengelolaanAkun.channel.connect(self.handleLamanPengelolaanAkun)
		self.lamanPermintaanPending.channel.connect(self.handleLamanPermintaanPending)

	def handleLamanPembayaran(self, nextPage):
		if (nextPage == "home"):
			self.mainWindow.setLaman()
			self.lamanPembayaran.close()
			self.mainWindow.show()
		elif (nextPage == "profile"):
			self.lamanPembayaran.close()
			self.lamanPengelolaanAkun.show()
		else:
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
		self.pageBuilder.close()
		self.lamanPermintaanDiterima.show()

	def handleFormLogin(self, nextPage):
		if (nextPage == "register"):
			self.formLogin.close()
			self.formRegister.show()
		elif(nextPage == "mainWindow"):
			self.mainWindow.setLaman()
			self.formLogin.close()
			self.mainWindow.show()
	
	def handleFormRegister(self):
		self.formRegister.close()
		self.formLogin.show()

	def handleMainWindow(self, nextPage, idLaman):
		if (nextPage == "riwayat_penggalangan_dana"):
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
			self.mainWindow.close()
			self.lamanRiwayatDonasi.show()
		elif (nextPage == "riwayat_penggalangan_dana"):
			self.mainWindow.close()
			self.lamanRiwayatPenggalanganDana.show()
		elif (nextPage == "eksplor"):
			self.lamanEksplor.setLaman()
			self.mainWindow.close()
			self.lamanEksplor.show()
		elif (nextPage == "permintaan"):
			pass
		else:
			pass
		
	def handleLamanRiwayatDonasi(self):
		self.lamanEksplor.setLaman()
		self.lamanRiwayatDonasi.close()
		self.lamanEksplor.show()

	def handleLamanRiwayatPenggalanganDana(self, nextPage):
		if (nextPage == "eksplor"):
			self.lamanEksplor.setLaman()
			self.lamanRiwayatPenggalanganDana.close()
			self.lamanEksplor.show()
		else:
			self.lamanRiwayatPenggalanganDana.close()
			self.lamanPenggalangDana.show()
			
	
	def handleLamanPengelolaanAkun(self, nextPage):
		self.mainWindow.setLaman()
		self.lamanPengelolaanAkun.close()
		self.mainWindow.show()

	def handleLamanPermintaanDiterima(self, nextPage):
		self.lamanPermintaanDiterima.close()
		if (nextPage == "pageBuilder"):
			self.pageBuilder.show()

	def handleLamanPermintaanPending(self, nextPage):
		self.lamanPermintaanPending.close()
		if (nextPage == "pageBuilder"):
			self.pageBuilder.show()
	
if __name__ == "__main__":
  app = QApplication(sys.argv)
  window = PageController()
#   window.show()
  sys.exit(app.exec())
