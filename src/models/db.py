from flask_mysqldb import MySQL

from config import databaseConfig
from application import app

app.config.from_object(databaseConfig)

mysql = MySQL(app)

# SETUP DDL
with app.app_context():
    cursor = mysql.connection.cursor()

    # DROP EXISTING TABLE
    cursor.execute("DROP TABLE IF EXISTS FotoLaman")
    cursor.execute("DROP TABLE IF EXISTS Laman")
    cursor.execute("DROP TABLE IF EXISTS PermintaanKesehatan")
    cursor.execute("DROP TABLE IF EXISTS PermintaanLainnya")
    cursor.execute("DROP TABLE IF EXISTS Permintaan")
    cursor.execute("DROP TABLE IF EXISTS AkunNoTelp")
    cursor.execute("DROP TABLE IF EXISTS Akun")

    # CREATE NEW TABLE
    # TABLE Akun
    cursor.execute("CREATE TABLE Akun ( \
                    IDPengguna INT UNSIGNED AUTO_INCREMENT, \
                    Email VARCHAR(320) UNIQUE NOT NULL, \
                    NamaDepan VARCHAR(255) NOT NULL, \
                    NamaBelakang VARCHAR(255) NOT NULL, \
                    Username VARCHAR(255) UNIQUE NOT NULL, \
                    Password VARBINARY(60) NOT NULL, \
                    Foto VARCHAR(255) DEFAULT NULL, \
                    PRIMARY KEY (IDPengguna))")
    # TABLE AkunNoTelp
    cursor.execute("CREATE TABLE AkunNoTelp ( \
                    IDPengguna INT UNSIGNED, \
                    NoTelp VARCHAR(31), \
                    PRIMARY KEY (IDPengguna, NoTelp), \
                    FOREIGN KEY (IDPengguna) REFERENCES Akun (IDPengguna) ON DELETE CASCADE)")
    # TABLE Permintaan
    cursor.execute("CREATE TABLE Permintaan (\
                    IDPermintaan INT UNSIGNED AUTO_INCREMENT,\
                    IDPengguna INT UNSIGNED,\
                    Judul VARCHAR(255) NOT NULL, \
                    Deskripsi VARCHAR(255) NOT NULL,\
                    Target BIGINT UNSIGNED,\
                    PRIMARY KEY (IDPermintaan),\
                    FOREIGN KEY (IDPengguna) REFERENCES Akun (IDPengguna) ON DELETE CASCADE)")
    # TABLE PermintaanKesehatan
    cursor.execute("CREATE TABLE PermintaanKesehatan (\
                    IDPermintaan INT UNSIGNED,\
                    FotoKTP VARCHAR(255) NOT NULL,\
                    FotoKK VARCHAR(255) NOT NULL,\
                    FotoSuratKeteranganMedis VARCHAR(255) NOT NULL,\
                    FotoHasilPemeriksaan VARCHAR(255) NOT NULL,\
                    Tujuan VARCHAR(255) NOT NULL,\
                    NamaPasien VARCHAR(255) NOT NULL,\
                    PRIMARY KEY (IDPermintaan),\
                    FOREIGN KEY (IDPermintaan) REFERENCES Permintaan (IDPermintaan) ON DELETE CASCADE)")
    # TABLE PermintaanLainnya
    cursor.execute("CREATE TABLE PermintaanLainnya (\
                    IDPermintaan INT UNSIGNED,\
                    Instansi VARCHAR(255) NOT NULL,\
                    AkunInstagram VARCHAR(255),\
                    AkunTwitter VARCHAR(255),\
                    AkunFacebook VARCHAR(255),\
                    PRIMARY KEY (IDPermintaan),\
                    FOREIGN KEY (IDPermintaan) REFERENCES Permintaan (IDPermintaan) ON DELETE CASCADE)")
    # TABLE Laman
    cursor.execute("CREATE TABLE Laman (\
                    IDLaman INT UNSIGNED AUTO_INCREMENT,\
                    IDAutentikasi INT UNSIGNED,\
                    IDPenggalang INT UNSIGNED,\
                    Judul VARCHAR(255) NOT NULL,\
                    Deskripsi VARCHAR(255) NOT NULL,\
                    Target  BIGINT UNSIGNED,\
                    Kategori VARCHAR(255) NOT NULL,\
                    Deadline DATE NOT NULL,\
                    Timestamp DATE NOT NULL,\
                    PRIMARY KEY (IDLaman),\
                    FOREIGN KEY (IDPenggalang) REFERENCES Akun (IDPengguna) ON DELETE CASCADE,\
                    FOREIGN KEY (IDAutentikasi) REFERENCES Permintaan (IDPermintaan) ON DELETE CASCADE)")
    # TABLE FotoLaman
    cursor.execute("CREATE TABLE FotoLaman (\
                    IDLaman INT UNSIGNED,\
                    Foto VARCHAR(255) NOT NULL,\
                    PRIMARY KEY (IDLaman, Foto),\
                    FOREIGN KEY (IDLaman) REFERENCES Laman (IDLaman) ON DELETE CASCADE)")

    mysql.connection.commit()
    cursor.close()