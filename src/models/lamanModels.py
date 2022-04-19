from datetime import datetime

from models.db import mysql
from models.cdn import bucket
import os

class Laman():
  # CONSTRUCTOR
  def __init__(self, idAutentikasi, idPenggalang, judul, deskripsi, target, kategori, deadline, foto):
    self.idAutentikasi = idAutentikasi
    self.idPenggalang = idPenggalang
    self.judul = judul
    self.deskripsi = deskripsi
    self.target = target
    self.kategori = kategori
    self.deadline = deadline
    self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # CHECK FOTO 
    listFoto = []
    for f in foto:
      blob = bucket.blob(f.filename)
      blob.upload_from_string(f.stream.read())
      listFoto.append(blob.public_url)

    self.foto = listFoto

    # INISIALIZE CURSOR
    cursor = mysql.connection.cursor()

    # INSERT Laman INTO DATABASE
    cursor.execute("INSERT INTO Laman (IDAutentikasi, IDPenggalang, Judul, Deskripsi, Target, Kategori, Deadline, Timestamp) \
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", (self.idAutentikasi, self.idPenggalang, self.judul, self.deskripsi, self.target, self.kategori, self.deadline, self.timestamp))

    self.idLaman = cursor.lastrowid

    # INSERT Foto INTO DATABASE
    for f in self.foto:
      cursor.execute("INSERT INTO LamanFoto (IDLaman, Foto) \
                      VALUES (%s, %s)", (self.idLaman, f))
    
    # CLOSE AND COMMIT CURSOR
    mysql.connection.commit()
    cursor.close()

  # CONSTRUCTOR BY IDLaman
  @classmethod
  def getByIDLaman(cls, idLaman):
    # INITIALIZE CURSOR
    cursor = mysql.connection.cursor()

    # SEARCH IDLaman
    cursor.execute("SELECT IDAutentikasi, IDPenggalang, Judul, Deskripsi, Target, Kategori, Deadline, Timestamp \
                    FROM Laman \
                    WHERE IDLaman = %s", (idLaman, ))
    
    dataLaman = cursor.fetchone()

    # SEARCH Foto by IDLaman
    cursor.execute("SELECT Foto \
                    FROM LamanFoto \
                    WHERE IDLaman = %s", (idLaman, ))
    
    dataFoto = cursor.fetchall()

    idAutentikasi, idPenggalang, judul, deskripsi, target, kategori, deadline, timestamp = dataLaman

    # initialize class
    self = cls.__new__(cls)
    self.idLaman = idLaman              #1
    self.idAutentikasi = idAutentikasi  #2
    self.idPenggalang = idPenggalang    #3
    self.judul = judul                  #4
    self.deskripsi = deskripsi          #5
    self.target = target                #6
    self.kategori = kategori            #7
    self.deadline = deadline            #8
    self.timestamp = timestamp          #9

    listFoto = []
    for foto in dataFoto:
      listFoto.append(foto)

    self.foto = listFoto                #10

    # CLOSE AND RETURN
    cursor.close()
    return self

  # CONSTRUCTOR BY Judul
  @classmethod
  def getByJudul(cls, queryJudul):
    # INITIALIZE CURSOR
    cursor = mysql.connection.cursor()
    # SEACH Judul CONTAINS queryJudul
    cursor.execute("SELECT * FROM Laman WHERE Judul LIKE %s", (f"%%{queryJudul}%%", ))

    dataLaman = cursor.fetchall()

    if len(dataLaman) == 0:
      cursor.close()
      return None

    else:
      listLaman = []
      for data in dataLaman:
        idLaman, idAutentikasi, idPenggalang, judul, deskripsi, target, kategori, deadline, timestamp = data

        # SEARCH Foto by IDLaman
        cursor.execute("SELECT Foto \
                        FROM LamanFoto \
                        WHERE IDLaman = %s", (idLaman, ))
        
        dataFoto = cursor.fetchall()

        # initialize class
        self = cls.__new__(cls)
        self.idLaman = idLaman              #1
        self.idAutentikasi = idAutentikasi  #2
        self.idPenggalang = idPenggalang    #3
        self.judul = judul                  #4
        self.deskripsi = deskripsi          #5
        self.target = target                #6
        self.kategori = kategori            #7
        self.deadline = deadline            #8
        self.timestamp = timestamp          #9

        listFoto = []
        for foto in dataFoto:
          listFoto.append(foto)

        self.foto = listFoto                #10
        listLaman.append(self)

      # CLOSE AND RETURN
      cursor.close()
      return listLaman

  # CONSTRUCTOR BY KATEGORI
  @classmethod
  def getByKategori(cls, kategori):
    # INITIALIZE CURSOR
    cursor = mysql.connection.cursor()
    # SEACH BY KATEGORI
    cursor.execute("SELECT * FROM Laman WHERE Kategori = %s", (kategori, ))

    dataLaman = cursor.fetchall()

    if len(dataLaman) == 0:
      cursor.close()
      return None
      
    else:
      listLaman = []
      for data in dataLaman:
        idLaman, idAutentikasi, idPenggalang, judul, deskripsi, target, kategori, deadline, timestamp = data

        # SEARCH Foto by IDLaman
        cursor.execute("SELECT Foto \
                        FROM LamanFoto \
                        WHERE IDLaman = %s", (idLaman, ))
        
        dataFoto = cursor.fetchall()

        # initialize class
        self = cls.__new__(cls)
        self.idLaman = idLaman              #1
        self.idAutentikasi = idAutentikasi  #2
        self.idPenggalang = idPenggalang    #3
        self.judul = judul                  #4
        self.deskripsi = deskripsi          #5
        self.target = target                #6
        self.kategori = kategori            #7
        self.deadline = deadline            #8
        self.timestamp = timestamp          #9

        listFoto = []
        for foto in dataFoto:
          listFoto.append(foto)

        self.foto = listFoto                #10
        listLaman.append(self)

      # CLOSE AND RETURN
      cursor.close()
      return listLaman

  # CONSTRUCTOR BY TotalDonasi
  @classmethod
  def getAll(cls):
    # INITIALIZE CURSOR
    cursor = mysql.connection.cursor()
    # SEACH TOTAL DONASI SORTED
    cursor.execute("SELECT * \
                    FROM Laman ")

    dataLaman = cursor.fetchall()

    if len(dataLaman) == 0:
      cursor.close()
      return None
    else:
      listLaman = []
      for data in dataLaman:
        idLaman, idAutentikasi, idPenggalang, judul, deskripsi, target, kategori, deadline, timestamp = data

        # SEARCH Foto by IDLaman
        cursor.execute("SELECT Foto \
                        FROM LamanFoto \
                        WHERE IDLaman = %s", (idLaman, ))
        
        dataFoto = cursor.fetchall()

        # initialize class
        self = cls.__new__(cls)
        self.idLaman = idLaman              #1
        self.idAutentikasi = idAutentikasi  #2
        self.idPenggalang = idPenggalang    #3
        self.judul = judul                  #4
        self.deskripsi = deskripsi          #5
        self.target = target                #6
        self.kategori = kategori            #7
        self.deadline = deadline            #8
        self.timestamp = timestamp          #9

        listFoto = []
        for foto in dataFoto:
          listFoto.append(foto)

        self.foto = listFoto                #10
        listLaman.append(self)

      # CLOSE AND RETURN
      cursor.close()
      return listLaman

  # CONSTRUCTOR BY IDPenggalang
  @classmethod
  def riwayatLaman(cls, idPenggalang):
        # INITIALIZE CURSOR
    cursor = mysql.connection.cursor()
    # SEACH TOTAL DONASI SORTED
    cursor.execute("SELECT * \
                    FROM Laman \
                    WHERE IDPenggalang = %s", (idPenggalang, ))

    dataLaman = cursor.fetchall()

    if len(dataLaman) == 0:
      cursor.close()
      return None
    else:
      listLaman = []
      for data in dataLaman:
        idLaman, idAutentikasi, idPenggalang, judul, deskripsi, target, kategori, deadline, timestamp = data

        # SEARCH Foto by IDLaman
        cursor.execute("SELECT Foto \
                        FROM LamanFoto \
                        WHERE IDLaman = %s", (idLaman, ))
        
        dataFoto = cursor.fetchall()

        # initialize class
        self = cls.__new__(cls)
        self.idLaman = idLaman              #1
        self.idAutentikasi = idAutentikasi  #2
        self.idPenggalang = idPenggalang    #3
        self.judul = judul                  #4
        self.deskripsi = deskripsi          #5
        self.target = target                #6
        self.kategori = kategori            #7
        self.deadline = deadline            #8
        self.timestamp = timestamp          #9

        listFoto = []
        for foto in dataFoto:
          listFoto.append(foto)

        self.foto = listFoto                #10
        listLaman.append(self)

      # CLOSE AND RETURN
      cursor.close()
      return listLaman

  # ATTRIBUTE METHOD
  def getIDLaman(self):
    return self.idLaman

  def getIDAutentikasi(self):
    return self.idAutentikasi

  def getIDPenggalang(self):
    return self.idPenggalang
  
  def getJudul(self):
    return self.judul

  def getDeskripsi(self):
    return self.deskripsi

  def getTarget(self):
    return self.target

  def getKategori(self):
    return self.kategori

  def getDeadline(self):
    return self.deadline

  def getTimestamp(self):
    return self.timestamp

  def getFoto(self):
    return self.foto

  # ATTRIBUTE SETTER

  def setFoto(self, dataFoto):
    listFoto = []
    for f in dataFoto:
      blob = bucket.blob(f.filename)
      blob.upload_from_string(f.stream.read())
      listFoto.append(blob.public_url)
    self.foto = listFoto

    # INITIALIZE CURSOR
    cursor = mysql.connection.cursor()

    # DELETE FOTO BEFORE
    cursor.execute("DELETE FROM LamanFoto \
                    WHERE IDLaman = %s", (self.idLaman, ))

    for foto in self.foto:
      # INSERT NEW FOTO
      cursor.execute("INSERT INTO LamanFoto (IDLaman, Foto) \
                      VALUES (%s, %s)", (self.idLaman, foto))

    # CLOSE AND COMMIT
    mysql.connection.commit()
    cursor.close()