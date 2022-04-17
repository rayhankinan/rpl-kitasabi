from models.db import mysql
from models.cdn import bucket
import sys

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
    cursor = mysql.connection.cursor()

    # INSERT TO TABLE Permintaan
    cursor.execute("INSERT INTO Permintaan (IDPengguna, Judul, Deskripsi, Target) \
                    VALUES (%s, %s, %s, %s)", (self.idPengguna, self.judul, self.deskripsi, self.target))

    # GET IDPermintaan
    self.idPermintaan = cursor.lastrowid
    # print(self.idPermintaan, file=sys.stdout)

    # CLOSE CURSOR
    mysql.connection.commit()
    cursor.close()

  # CONSTRUCTOR BY IDPermintaan
  @classmethod
  def getByIDPermintaan(cls, idPermintaan):
    # INITIALIZE CURSOR
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT IDPengguna, Judul, Deskripsi, Target, StatusAutentikasi\
                    FROM Permintaan \
                    WHERE IDPermintaan = %s", (idPermintaan))

    dataPermintaan = cursor.fetchone()
    cursor.close()

    if dataPermintaan is None:
      raise Exception(f"IDPermintaan {idPermintaan} tidak ada!")
    else:
      idPengguna, judul, deskripsi, target, statusAutentikasi = dataPermintaan

      self = cls.__new__(cls)
      self.idPermintaan = idPermintaan
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
    cursor.execute("SELECT IDPermintaan, Judul, Deskripsi, Target, StatusAutentikasi\
                    FROM Permintaan \
                    WHERE IDPengguna = %s", (idPengguna, ))

    dataPermintaan = cursor.fetchall()

    if len(dataPermintaan) == 0:
      return None
    else:
      listPermintaan = []

      for data in dataPermintaan:
        idPermintaan, judul, deskripsi, target, statusAutentikasi = data

        self = cls.__new__(cls)
        self.idPermintaan = idPermintaan          #1
        self.idPengguna = idPengguna              #2
        self.judul = judul                        #3
        self.deskripsi = deskripsi                #4
        self.target = target                      #5
        self.statusAutentikasi = statusAutentikasi#6

        listPermintaan.append(self)

      cursor.close()
      return listPermintaan

  # ATTRIBUTE METHOD
  def getIDPermintaan(self):
    return self.idPermintaan

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
                    WHERE IdPermintaan = %s", (self.statusAutentikasi, self.idPermintaan))
    # CLOSE AND COMMIT CURSOR
    mysql.connection.commit()
    cursor.close()

class PermintaanKesehatan(Permintaan):
  # CONSTRUCTOR
  def __init__(self, idPengguna, judul, deskripsi, target, fotoKTP, fotoKK, fotoKetMedis, fotoPemeriksan, tujuan, namaPasien):
    Permintaan.__init__(self, idPengguna, judul, deskripsi, target)
    
    # CHECK
    self.tujuan = tujuan
    self.namaPasien = namaPasien

    # FOTO KTP
    if fotoKTP is not None:
      ktpBlob = bucket.blob(fotoKTP.filename)
      ktpBlob.upload_from_string(fotoKTP.stream.read())
      self.fotoKTP = ktpBlob.public_url
    else:
      self.fotoKTP = None

    # FOTO KK
    if fotoKK is not None:
      kkBlob = bucket.blob(fotoKK.filename)
      kkBlob.upload_from_string(fotoKK.stream.read())
      self.fotoKK = kkBlob.public_url
    else:
      self.fotoKK = None

    # FOTO KET MEDIS
    if fotoKetMedis is not None:
      ketMedisBlob = bucket.blob(fotoKetMedis.filename)
      ketMedisBlob.upload_from_string(fotoKetMedis.stream.read())
      self.fotoKetMedis = ketMedisBlob.public_url
    else:
      self.fotoKetMedis = None
    
    # FOTO PEMERIKSAAN
    if fotoPemeriksan is not None:
      pemeriksaanBlob = bucket.blob(fotoPemeriksan.filename)
      pemeriksaanBlob.upload_from_string(fotoPemeriksan.stream.read())
      self.fotoPemeriksaan = pemeriksaanBlob.public_url
    else:
      self.fotoPemeriksaan = None


    # INITIALIZE CURSOR 
    cursor = mysql.connection.cursor()
    
    # INSERT TO DB
    cursor.execute("INSERT INTO PermintaanKesehatan \
                    (IDPermintaanKesehatan, FotoKTP, FotoKK, FotoSuratKeteranganMedis, FotoHasilPemeriksaan, Tujuan, NamaPasien) \
                    VALUES (%s, %s, %s, %s, %s, %s, %s)", (self.idPermintaan, self.fotoKTP, self.fotoKK, self.fotoKetMedis, self.fotoPemeriksaan, self.tujuan, self.namaPasien))

    # CLOSE CURSOR
    mysql.connection.commit()
    cursor.close()

  # CONSTRUCTOR BY IDPermintaan
  @classmethod
  def getByIDPermintaanKesehatan (cls, idPermintaanKesehatan):
    # INITIALIZE CURSOR
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT FotoKTP, FotoKK, FotoSuratKeteranganMedis, FotoHasilPemeriksaan, Tujuan, NamaPasien \
                    FROM PermintaanKesehatan \
                    WHERE IDPermintaanKesehatan = %s", (idPermintaanKesehatan))

    dataPermintaan = Permintaan.getByIDPermintaan(idPermintaanKesehatan)
    dataPermintaanKesehatan = cursor.fetchone()
    cursor.close()

    if dataPermintaanKesehatan is None:
      raise Exception(f"IDPermintaanKesehatan {idPermintaanKesehatan} tidak ada!")
    else:
      idPengguna = dataPermintaan.idPengguna
      judul = dataPermintaan.judul
      deskripsi = dataPermintaan.deskripsi
      target = dataPermintaan.target
      statusAutentikasi = dataPermintaan.statusAutentikasi

      fotoKTP, fotoKK, fotoKetMedis, fotoPemeriksan, tujuan, namaPasien = dataPermintaanKesehatan;

      self = cls.__new__(cls)
      self.idPermintaan = idPermintaanKesehatan #1
      self.idPengguna = idPengguna              #2
      self.judul = judul                        #3
      self.deskripsi = deskripsi                #4
      self.target = target                      #5
      self.statusAutentikasi = statusAutentikasi#6
      self.tujuan = tujuan                      #7
      self.namaPasien = namaPasien              #8
      self.fotoKTP = fotoKTP                    #9
      self.fotoKK = fotoKK                      #10
      self.fotoKetMedis = fotoKetMedis          #11
      self.fotoPemeriksaan = fotoPemeriksan     #12

      return self

  # CONSTRUCTOR BY IDPengguna
  @classmethod
  def getByIDPengguna(cls, idPengguna):
    # INITIALIZE CURSOR
    cursor = mysql.connection.cursor()

    dataPermintaan = Permintaan.getByIDPengguna(idPengguna)
    print(len(dataPermintaan), file=sys.stdout)

    if dataPermintaan is None:
      return None
    else:
      listPermintaan = []

      for data in dataPermintaan:
        idPermintaan = data.idPermintaan
        judul = data.judul
        deskripsi = data.deskripsi
        target = data.target
        statusAutentikasi = data.statusAutentikasi

        # SELECT PermintaanKesehatan BY IDPermintaan
        cursor.execute("SELECT FotoKTP, FotoKK, FotoSuratKeteranganMedis, FotoHasilPemeriksaan, Tujuan, NamaPasien\
                        FROM PermintaanKesehatan \
                        WHERE IdPermintaanKesehatan = %s", (idPermintaan, ))

        dataPermintaanKesehatan = cursor.fetchone();
        if (dataPermintaanKesehatan is not None):
          fotoKTP, fotoKK, fotoKetMedis, fotoPemeriksan, tujuan, namaPasien = dataPermintaanKesehatan;

          self = cls.__new__(cls)
          self.idPermintaan = idPermintaan          #1
          self.idPengguna = idPengguna              #2
          self.judul = judul                        #3
          self.deskripsi = deskripsi                #4
          self.target = target                      #5
          self.statusAutentikasi = statusAutentikasi#6
          self.tujuan = tujuan                      #7
          self.namaPasien = namaPasien              #8
          self.fotoKTP = fotoKTP                    #9
          self.fotoKK = fotoKK                      #10
          self.fotoKetMedis = fotoKetMedis          #11
          self.fotoPemeriksaan = fotoPemeriksan     #12

          listPermintaan.append(self)

      cursor.close()

      if (len(listPermintaan) == 0):
        return None
      else:
        return listPermintaan

  # ATTRIBUTE METHOD
  def getFotoKTP(self):
    return self.fotoKTP

  def getFotoKK(self):
    return self.fotoKK

  def getFotoKetMedis(self):
    return self.fotoKetMedis

  def getFotoPemeriksaan(self):
    return self.fotoPemeriksaan

  def getTujuan(self):
    return self.tujuan

  def getNamaPasien(self):
    return self.namaPasien

class PermintaanLainnya(Permintaan):

  # CONSTRUCTOR
  def __init__(self, idPengguna, judul, deskripsi, target, instansi, ig, twt, fb):
    Permintaan.__init__(self,idPengguna, judul, deskripsi, target)

    # INITIALIZE ATTRIBUTE
    self.instansi = instansi
    self.instagram = ig
    self.twitter = twt
    self.facebook = fb

    # INITTIALIZE CURSOR
    cursor = mysql.connection.cursor()

    # INSERT INTO DB
    cursor.execute("INSERT INTO PermintaanLainnya (IDPermintaanLainnya, Instansi, AkunInstagram, AkunTwitter, AkunFacebook) \
                    VALUES (%s, %s, %s, %s, %s)", (self.idPermintaan, self.instansi, self.instagram, self.twitter, self.facebook))
    mysql.connection.commit()

    # CLOSE DB
    cursor.close()

  # CONSTRUCTOR BY IdPermintaan
  @classmethod
  def getByIDPermintaanLainnya(cls, idPermintaanLainnya):
    # INITIALIZE CURSOR
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT Instansi, AkunInstagram, AkunTwitter, AkunFacebook \
                    FROM PermintaanLainnya \
                    WHERE IDPermintaanLainnya = %s", (idPermintaanLainnya, ))

    dataPermintaan = Permintaan.getByIDPermintaan(idPermintaanLainnya)
    dataPermintaanLainnya = cursor.fetchone()
    cursor.close()

    if dataPermintaanLainnya is None:
      raise Exception(f"IDPermintaanLainnya {idPermintaanLainnya} tidak ada!")
    else:
      # CREATE INSTANCES
      idPengguna = dataPermintaan.idPengguna
      judul = dataPermintaan.judul
      deskripsi = dataPermintaan.deskripsi
      target = dataPermintaan.target
      statusAutentikasi = dataPermintaan.statusAutentikasi

      instansi, ig, twt, fb = dataPermintaanLainnya;

      self = cls.__new__(cls)
      self.idPermintaan = idPermintaanLainnya   #1
      self.idPengguna = idPengguna              #2
      self.judul = judul                        #3
      self.deskripsi = deskripsi                #4
      self.target = target                      #5
      self.statusAutentikasi = statusAutentikasi#6
      self.instansi = instansi                  #7
      self.instagram = ig                       #8
      self.twitter = twt                        #9
      self.facebook = fb                        #10

      return self

  # CONSTRUCTOR BY IDPengguna
  @classmethod
  def getByIDPengguna(cls, idPengguna):
    # INITIALIZE CURSOR
    cursor = mysql.connection.cursor()

    dataPermintaan = Permintaan.getByIDPengguna(idPengguna)
    print(dataPermintaan, file=sys.stdout)

    if dataPermintaan is None:
      return None
    else:
      listPermintaan = []

      for data in dataPermintaan:
        idPermintaan = data.idPermintaan
        judul = data.judul
        deskripsi = data.deskripsi
        target = data.target
        statusAutentikasi = data.statusAutentikasi

        # SELECT PermintaanLainnya BY IDPermintaan
        cursor.execute("SELECT Instansi, AkunInstagram, AkunTwitter, AkunFacebook \
                        FROM PermintaanLainnya \
                        WHERE IdPermintaanLainnya = %s", (idPermintaan, ))

        dataPermintaanLainnya = cursor.fetchone();

        if (dataPermintaanLainnya is not None):
          instansi, ig, twt, fb = dataPermintaanLainnya;

          self = cls.__new__(cls)
          self.idPermintaan = idPermintaan          #1
          self.idPengguna = idPengguna              #2
          self.judul = judul                        #3
          self.deskripsi = deskripsi                #4
          self.target = target                      #5
          self.statusAutentikasi = statusAutentikasi#6
          self.instansi = instansi                  #7
          self.instagram = ig                       #8
          self.twitter = twt                        #9
          self.facebook = fb                        #10

          listPermintaan.append(self)

      cursor.close()
      return listPermintaan

  # ATTRIBUTE METHOD
  def getInstansi(self):
    return self.instansi

  def getAkunInstagram(self):
    return self.instagram

  def getAkunTwitter(self):
    return self.twitter

  def getAkunFacebook(self):
    return self.facebook