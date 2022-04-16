import imp
from models.db import mysql

class Transaksi:
    # CONSTRUCTOR
    def __init__(self, idDonatur, idLaman, jumlahTransaksi):
        self.idDonatur = idDonatur
        self.idLaman = idLaman
        self.jumlahTransaksi = jumlahTransaksi

        # INISIALISASI CURSOR
        cursor = mysql.connection.cursor()

        # MASUKKAN TRANSAKSI KE DALAM DATABASE
        cursor.execute("INSERT INTO Transaksi (IDDonatur, IDLaman, JumlahTransaksi) VALUES (%d, %d, %d)", (self.idDonatur, self.idLaman, self.jumlahTransaksi))
        
        # TUTUP CURSOR
        mysql.connection.commit()
        cursor.close()