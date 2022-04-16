from os import EX_CANTCREAT

from MySQLdb import MySQLError
from models.db import mysql
from models.cdn import bucket

class Permintaan:
  # CONSTRUCTOR
  def __init__(self, idPengguna, judul, deskripsi, target):
    # INITIALIZE ATTRIBUTE
    self.idPengguna = idPengguna
    self.judul = judul
    self.deskripsi = deskripsi
    self.statusAutentikasi = False

    if (target <= 0):
      raise Exception(f"{target} bukanlah target yang valid!")
    else:
      self.target = target

    # INITIALIZE CURSOR
    cursor = mysql.connecttion.cursor()

    # INSERT TO TABLE Permintaan
    cursor.execute("INSERT INTO Permintaan \
                    (IDPengguna, Judul, Deskripsi, Target, StatusAutentikasi) \
                    VALUES (%d, %s, %s, %d)", (self.idPengguna, self.judul, self.judul, self.target, self.statusAutentikasi))

    # CLOSE CURSOR
    mysql.connection.commit()
    cursor.close()

  # CONSTRUCTOR BY IDPermintaan
  @classmethod
  def getByJudulAndDeskripsi(cls, judul, deskripsi):
    # INITIALIZE CURSOR
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT IDPengguna, Judul, Deskripsi, Target, StatusAutentikasi\
                    FROM Permintaan \
                    WHERE Judul = %s \
                    WHERE Deskripsi = %s", (self.judul, self.deskripsi))


    dataPermintaan = cursor.fetchone()
    cursor.close()

    if dataPermintaan is None:
      raise Exception("Judul dan Deskripsi tidak ada!")
    else:
      idPengguna, judul, deskripsi, target, statusAutentikasi = dataPermintaan

      self = cls.__new__(cls)
      self.idPengguna = idPengguna
      self.judul = judul
      self.deskripsi = deskripsi
      self.target = target
      self.statusAutentikasi = statusAutentikasi

      return self

  # CONSTRUCTOR BY IDPengguna
  @classmethod
  def getByIDPengguna(cls, idPengguna):
    # INITIALIZE CURSOR
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT Judul, Deskripsi, Target, StatusAutentikasi\
                    FROM Permintaan \
                    WHERE IDPengguna = %s", (idPengguna))

    dataPermintaan = cursor.fetchall()
    cursor.close()

    if dataPermintaan is None:
      raise Exception(f"IDPengguna {idPengguna} tidak memiliki permintaan penggalangan dana!")
    else:
      listPermintaan = []

      for data in dataPermintaan:
        judul, deskripsi, target, statusAutentikasi = data
        self = cls.__new__(cls)
        self.idPengguna = idPengguna
        self.judul = judul
        self.deskripsi = deskripsi
        self.target = target
        self.statusAutentikasi = statusAutentikasi

        listPermintaan.append(self)

      return listPermintaan

  # ATTRIBUTE METHOD
  def getIDPengguna(self):
    return self.idPengguna

  def getJudul(self):
    return self.judul

  def getDeskripsi(self):
    return self.deskripsi

  def getTarget(self):
    return self.target

  def getStatusAutentikasi(self):
    return self.statusAutentikasi

  def setStatusAutentikasi(self, status):
    # UPDATE ATTRIBUTE
    self.statusAutentikasi = status

    # INISIALISASI CURSOR
    cursor = mysql.connection.cursor()
    cursor.execute("UPDATE Permintaan \
                    SET StatusAutentikasi = %s \
                    WHERE Judul = %s \
                    WHERE Deskripsi = %s", (self.statusAutentikasi, self.judul, self.deskripsi))

    # CLOSE CURSOR
    mysql.connection.commit()
    cursor.close()

class PermintaanKesehatan(Permintaan):
  # CONSTRUCTOR
  def __init__(self, idPengguna, judul, deskripsi, target, idPermintaan, fotoKTP, fotoKK, fotoKetMedis, fotoPemeriksan, tujuan, namaPasien):
    super().init(idPengguna, judul, deskripsi, target)

    # CHECK
    self.idPermintaan = idPermintaan
    self.tujuan = tujuan

    # FOTO KTP
    ktpBlob = bucket.blob(fotoKTP.filename)
    ktpBlob.upload_from_string(fotoKTP.stream.read())
    self.fotoKTP = ktpBlob.public_url

    # FOTO KK
    kkBlob = bucket.blob(fotoKK.filename)
    kkBlob.upload_from_string(fotoKK.stream.read())
    self.fotoKK = kkBlob.public_url

    # FOTO KET MEDIS
    ketMedisBlob = bucket.blob(fotoKetMedis.filename)
    ketMedisBlob.upload_from_string(fotoKetMedis.stream.read())
    self.fotoKetMedis = ketMedisBlob.public_url
    
    # FOTO PEMERIKSAAN
    pemeriksaanBlob = bucket.blob(fotoPemeriksan.filename)
    pemeriksaanBlob.upload_from_string(fotoPemeriksan.stream.read())
    self.fotoPemeriksaan = pemeriksaanBlob.public_url

    if not namaPasien.isalnum():
      raise Exception(f"{namaPasien} bukanlah nama yang valid!")
    else:
      self.namaPasien = namaPasien

    # INITIALIZE CURSOR 
    cursor = mysql.connection.cursor()
    
    # INSERT TO DB
    cursor.execute("INSERT INTO PermintaanKesehatan \
                    (IDPermintaan, FotoKTP, FotoKK, FotoSuratKeteranganMedis, FotoHasilPemeriksaan, Tujuan, NamaPasien) \
                    VALUES (%d, %s, %s, %s, %s, %s)", (self.idPermintaan, self.fotoKTP, self.fotoKK, self.fotoPemeriksaan, self.tujuan, self.namaPasien))

    # CLOSE CURSOR
    mysql.connection.commit()
    cursor.close()

  # CONSTRUCTOR BY IDPermintaan
  @classmethod
  def getByIDPermintaan(cls, idPermintaan):
    # INITIALIZE CURSOR
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT FotoKTP, FotoKK, FotoSuratKeteranganMedis, FotoHasilPemeriksaan, Tujuan, NamaPasien \
                    FROM PermintaanKesehatan \
                    WHERE IDPermintaan = %d", (idPermintaan))

    dataPermintaan = Permintaan.getByIDPermintaan(idPermintaan)
    dataPermintaanKesehatan = cursor.fecthone()
    cursor.close()

    if dataPermintaanKesehatan is None:
      raise Exception(f"IDPermintaan {idPermintaan} tidak ada!")
    else:
      idPengguna = dataPermintaan.idPengguna
      judul = dataPermintaan.judul
      deskripsi = dataPermintaan.deskripsi
      target = dataPermintaan.target

      fotoKTP, fotoKK, fotoKetMedis, fotoPemeriksan, tujuan, namaPasien = dataPermintaanKesehatan;

      self = cls.__new__(cls)
      self.idPengguna = idPengguna
      self.judul = judul
      self.deskripsi = deskripsi
      self.target = target
      self.idPermintaan = idPermintaan
      self.tujuan = tujuan
      self.namaPasien = namaPasien

      # FOTO KTP
      ktpBlob = bucket.blob(fotoKTP.filename)
      ktpBlob.upload_from_string(fotoKTP.stream.read())
      self.fotoKTP = ktpBlob.public_url

      # FOTO KK
      kkBlob = bucket.blob(fotoKK.filename)
      kkBlob.upload_from_string(fotoKK.stream.read())
      self.fotoKK = kkBlob.public_url

      # FOTO KET MEDIS
      ketMedisBlob = bucket.blob(fotoKetMedis.filename)
      ketMedisBlob.upload_from_string(fotoKetMedis.stream.read())
      self.fotoKetMedis = ketMedisBlob.public_url
      
      # FOTO PEMERIKSAAN
      pemeriksaanBlob = bucket.blob(fotoPemeriksan.filename)
      pemeriksaanBlob.upload_from_string(fotoPemeriksan.stream.read())
      self.fotoPemeriksaan = pemeriksaanBlob.public_url

      return self

  

