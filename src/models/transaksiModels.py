from datetime import datetime

from models.db import mysql

class Transaksi:
    # CONSTRUCTOR
    def __init__(self, idDonatur, idLaman, jumlahTransaksi):
        self.idDonatur = idDonatur
        self.idLaman = idLaman
        self.jumlahTransaksi = jumlahTransaksi
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.statusPencairan = False

        # INISIALISASI CURSOR
        cursor = mysql.connection.cursor()

        # MASUKKAN TRANSAKSI KE DALAM DATABASE
        cursor.execute("INSERT INTO Transaksi (IDDonatur, IDLaman, JumlahTransaksi) VALUES (%d, %d, %d)", (self.idDonatur, self.idLaman, self.jumlahTransaksi))
        
        # TUTUP CURSOR
        mysql.connection.commit()
        cursor.close()

    # STATIC METHOD
    @staticmethod
    def getTotalByLaman(idLaman):
        cursor = mysql.connection.cursor()

        cursor.execute("SELECT SUM(JumlahTransaksi) FROM Transaksi WHERE IDLaman = %d AND NOT StatusPencairan GROUP BY IDLaman", (idLaman, ))
        dataTotalTransaksi = cursor.fetchone()

        cursor.close()

        totalTransaksi, = dataTotalTransaksi
        return totalTransaksi

    # CLASS METHOD
    @classmethod
    def getRiwayatDonasi(cls, id):
        cursor = mysql.connection.cursor()

        cursor.execute("SELECT IDDonatur, IDLaman, JumlahTransaksi, Timestamp, StatusPencairan FROM Transaksi WHERE IDDonatur = %d", (id, ))
        dataRiwayat = cursor.fetchall()

        cursor.close()

        riwayat = []
        for row in dataRiwayat:
            idDonatur, idLaman, jumlahTransaksi, timestamp, statusPencairan = row

            self = cls.__new__(cls)
            self.idDonatur = idDonatur
            self.idLaman = idLaman
            self.jumlahTransaksi = jumlahTransaksi
            self.timestamp = timestamp
            self.statusPencairan = statusPencairan

            riwayat.append(self)

        return riwayat


    @classmethod
    def getRiwayatLaman(cls, id):
        cursor = mysql.connection.cursor()

        cursor.execute("SELECT IDDonatur, IDLaman, JumlahTransaksi, Timestamp, StatusPencairan FROM Transaksi WHERE IDLaman = %d", (id, ))
        dataRiwayat = cursor.fetchall()

        cursor.close()

        riwayat = []
        for row in dataRiwayat:
            idDonatur, idLaman, jumlahTransaksi, timestamp, statusPencairan = row

            self = cls.__new__(cls)
            self.idDonatur = idDonatur
            self.idLaman = idLaman
            self.jumlahTransaksi = jumlahTransaksi
            self.timestamp = timestamp
            self.statusPencairan = statusPencairan

            riwayat.append(self)

        return riwayat

    # ATTRIBUTE METHOD
    def getIDDonatur(self):
        return self.idDonatur

    def getIDLaman(self):
        return self.idLaman

    def getJumlahTransaksi(self):
        return self.jumlahTransaksi

    def getTimestamp(self):
        return self.timestamp

    def getStatusPencairan(self):
        return self.statusPencairan

    def cairkanTransaksi(self):
        if self.statusPencairan:
            raise Exception("Transaksi sudah dicairkan!")
        else:
            self.statusPencairan = True