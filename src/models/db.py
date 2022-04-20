from flask_mysqldb import MySQL

from config import databaseConfig
from application import app

app.config.from_object(databaseConfig)

mysql = MySQL(app)

# SETUP DDL
with app.app_context():
    cursor = mysql.connection.cursor()

    # DROP EXISTING TABLE
    cursor.execute("DROP TABLE IF EXISTS Transaksi")
    cursor.execute("DROP TABLE IF EXISTS LamanFoto")
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
                    Foto VARCHAR(255) NOT NULL, \
                    PRIMARY KEY (IDPengguna))")

    # TABLE AkunNoTelp
    cursor.execute("CREATE TABLE AkunNoTelp ( \
                    IDPengguna INT UNSIGNED, \
                    NoTelp VARCHAR(31), \
                    PRIMARY KEY (IDPengguna, NoTelp), \
                    FOREIGN KEY (IDPengguna) REFERENCES Akun (IDPengguna) ON DELETE CASCADE)")

    # TABLE Permintaan
    cursor.execute("CREATE TABLE Permintaan ( \
                    IDPermintaan INT UNSIGNED AUTO_INCREMENT,\
                    IDPengguna INT UNSIGNED NOT NULL,\
                    Judul VARCHAR(255) NOT NULL, \
                    Deskripsi VARCHAR(255) NOT NULL, \
                    Target BIGINT UNSIGNED NOT NULL, \
                    StatusAutentikasi BOOLEAN DEFAULT NULL, \
                    UNIQUE (Judul, Deskripsi), \
                    PRIMARY KEY (IDPermintaan), \
                    FOREIGN KEY (IDPengguna) REFERENCES Akun (IDPengguna) ON DELETE CASCADE)")

    # TABLE PermintaanKesehatan
    cursor.execute("CREATE TABLE PermintaanKesehatan ( \
                    IDPermintaanKesehatan INT UNSIGNED, \
                    FotoKTP VARCHAR(255) NOT NULL, \
                    FotoKK VARCHAR(255) NOT NULL, \
                    FotoSuratKeteranganMedis VARCHAR(255) NOT NULL, \
                    FotoHasilPemeriksaan VARCHAR(255) NOT NULL, \
                    Tujuan VARCHAR(255) NOT NULL, \
                    NamaPasien VARCHAR(255) NOT NULL, \
                    PRIMARY KEY (IDPermintaanKesehatan), \
                    FOREIGN KEY (IDPermintaanKesehatan) REFERENCES Permintaan (IDPermintaan) ON DELETE CASCADE)")

    # TABLE PermintaanLainnya
    cursor.execute("CREATE TABLE PermintaanLainnya ( \
                    IDPermintaanLainnya INT UNSIGNED, \
                    Instansi VARCHAR(255) NOT NULL, \
                    AkunInstagram VARCHAR(255), \
                    AkunTwitter VARCHAR(255), \
                    AkunFacebook VARCHAR(255), \
                    NamaPenerima VARCHAR(255) NOT NULL, \
                    PRIMARY KEY (IDPermintaanLainnya), \
                    FOREIGN KEY (IDPermintaanLainnya) REFERENCES Permintaan (IDPermintaan) ON DELETE CASCADE)")
                    
    # TABLE Laman
    cursor.execute("CREATE TABLE Laman ( \
                    IDLaman INT UNSIGNED AUTO_INCREMENT, \
                    IDAutentikasi INT UNSIGNED NOT NULL, \
                    IDPenggalang INT UNSIGNED NOT NULL, \
                    Judul VARCHAR(255) NOT NULL, \
                    Deskripsi VARCHAR(255) NOT NULL, \
                    Target BIGINT UNSIGNED NOT NULL, \
                    Kategori ENUM('Kesehatan', 'Lainnya') NOT NULL, \
                    Deadline DATE NOT NULL, \
                    Timestamp DATETIME NOT NULL, \
                    PRIMARY KEY (IDLaman), \
                    FOREIGN KEY (IDPenggalang) REFERENCES Akun (IDPengguna) ON DELETE CASCADE, \
                    FOREIGN KEY (IDAutentikasi) REFERENCES Permintaan (IDPermintaan) ON DELETE CASCADE)")

    # TABLE FotoLaman
    cursor.execute("CREATE TABLE LamanFoto ( \
                    IDLaman INT UNSIGNED, \
                    Foto VARCHAR(255) NOT NULL, \
                    PRIMARY KEY (IDLaman, Foto), \
                    FOREIGN KEY (IDLaman) REFERENCES Laman (IDLaman) ON DELETE CASCADE)")

    # TABLE Transaksi
    cursor.execute("CREATE TABLE Transaksi ( \
                    IDTransaksi INT UNSIGNED AUTO_INCREMENT, \
                    IDDonatur INT UNSIGNED, \
                    IDLaman INT UNSIGNED, \
                    JumlahTransaksi BIGINT UNSIGNED NOT NULL, \
                    Timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP() NOT NULL, \
                    StatusPencairan BOOLEAN DEFAULT FALSE NOT NULL, \
                    PRIMARY KEY (IDTransaksi), \
                    FOREIGN KEY (IDDonatur) REFERENCES Akun (IDPengguna) ON DELETE SET NULL, \
                    FOREIGN KEY (IDLaman) REFERENCES Laman (IDLaman) ON DELETE SET NULL, \
                    UNIQUE (IDDonatur, IDLaman, Timestamp))")

    # DUMMY DATA AKUN
    cursor.execute("INSERT INTO Akun (Email, NamaDepan, NamaBelakang, Username, Password, Foto) \
                    VALUES (%s, %s, %s, %s, %s, %s)", ("kitasabi@kitasabi.com", "kita", "sabi", "kitasabi",  "$2b$12$oACTLwRomSp0vWcxo.NrSOnDNoT4YmX0gQ0moSdhM700OvJd74XDG", "https://storage.googleapis.com/kitasabi-images/kitasabi.jpeg"))
    
    cursor.execute("INSERT INTO AkunNoTelp \
                    VALUES (%s, %s)", (1, "+6285322382578"))

    # DUMMY Permintaan Kesehatan
    cursor.execute("INSERT INTO Permintaan (IDPengguna, Judul, Deskripsi, Target, StatusAutentikasi) \
                    VALUES (%s, %s, %s, %s, %s)", (1, "Dummy Permintaan 1", "CERITANYA DESKRIPSI DUMMPY PERMINTAAN 1", 20000, 1))

    cursor.execute("INSERT INTO PermintaanKesehatan \
                    (IDPermintaanKesehatan, FotoKTP, FotoKK, FotoSuratKeteranganMedis, FotoHasilPemeriksaan, Tujuan, NamaPasien) \
                    VALUES (%s, %s, %s, %s, %s, %s, %s)", (1, "https://storage.googleapis.com/kitasabi-images/foto-ktp", " https://storage.googleapis.com/kitasabi-images/foto-kk", "https://storage.googleapis.com/kitasabi-images/foto-ket-medis", "https://storage.googleapis.com/kitasabi-images/foto-pemeriksaan", "TUJUANNYA BIAR RPL A", "SARAH ASKA ORANG SAKIT"))

    cursor.execute("INSERT INTO Permintaan (IDPengguna, Judul, Deskripsi, Target, StatusAutentikasi) \
                    VALUES (%s, %s, %s, %s, %s)", (1, "Dummy Permintaan 2", "CERITANYA DESKRIPSI DUMMPY PERMINTAAN 2", 30000, 1))

    cursor.execute("INSERT INTO PermintaanKesehatan \
                    (IDPermintaanKesehatan, FotoKTP, FotoKK, FotoSuratKeteranganMedis, FotoHasilPemeriksaan, Tujuan, NamaPasien) \
                    VALUES (%s, %s, %s, %s, %s, %s, %s)", (2, "https://storage.googleapis.com/kitasabi-images/foto-ktp", " https://storage.googleapis.com/kitasabi-images/foto-kk", "https://storage.googleapis.com/kitasabi-images/foto-ket-medis", "https://storage.googleapis.com/kitasabi-images/foto-pemeriksaan", "TUJUANNYA BIAR RPL A", "FIKRI FIKRON ORANG SAKIT"))

    cursor.execute("INSERT INTO Permintaan (IDPengguna, Judul, Deskripsi, Target, StatusAutentikasi) \
                    VALUES (%s, %s, %s, %s, %s)", (1, "Dummy Permintaan 3", "CERITANYA DESKRIPSI DUMMPY PERMINTAAN 3", 40000, 0))

    cursor.execute("INSERT INTO PermintaanKesehatan \
                    (IDPermintaanKesehatan, FotoKTP, FotoKK, FotoSuratKeteranganMedis, FotoHasilPemeriksaan, Tujuan, NamaPasien) \
                    VALUES (%s, %s, %s, %s, %s, %s, %s)", (3, "https://storage.googleapis.com/kitasabi-images/foto-ktp", " https://storage.googleapis.com/kitasabi-images/foto-kk", "https://storage.googleapis.com/kitasabi-images/foto-ket-medis", "https://storage.googleapis.com/kitasabi-images/foto-pemeriksaan", "TUJUANNYA BIAR RPL A", "RAYHAN KONAN ORANG SAKIT"))

    # DUMMY Permintaan Lainnya
    cursor.execute("INSERT INTO Permintaan (IDPengguna, Judul, Deskripsi, Target, StatusAutentikasi) \
                    VALUES (%s, %s, %s, %s, %s)", (1, "Dummy Permintaan 4", "CERITANYA DESKRIPSI DUMMPY PERMINTAAN 4", 50000, 1))

    cursor.execute("INSERT INTO PermintaanLainnya (IDPermintaanLainnya, Instansi, AkunInstagram, AkunTwitter, AkunFacebook, NamaPenerima) \
                    VALUES (%s, %s, %s, %s, %s, %s)", (4, "KITASABI", "@kitasabi", "@kitasabi", "kitasabi sabi sabi sabi bos", "DAH GATAU NAMANY SYP"))

    cursor.execute("INSERT INTO Permintaan (IDPengguna, Judul, Deskripsi, Target, StatusAutentikasi) \
                    VALUES (%s, %s, %s, %s, %s)", (1, "Dummy Permintaan 5", "CERITANYA DESKRIPSI DUMMPY PERMINTAAN 5", 50000, 0))

    cursor.execute("INSERT INTO PermintaanLainnya (IDPermintaanLainnya, Instansi, AkunInstagram, AkunTwitter, AkunFacebook, NamaPenerima) \
                    VALUES (%s, %s, %s, %s, %s, %s)", (5, "KITASABI", "@kitasabi", "@kitasabi", "kitasabi sabi sabi sabi bos", "siapa y"))

    cursor.execute("INSERT INTO Permintaan (IDPengguna, Judul, Deskripsi, Target, StatusAutentikasi) \
                    VALUES (%s, %s, %s, %s, %s)", (1, "Dummy Permintaan 6", "CERITANYA DESKRIPSI DUMMPY PERMINTAAN 6", 50000, 0))

    cursor.execute("INSERT INTO PermintaanLainnya (IDPermintaanLainnya, Instansi, AkunInstagram, AkunTwitter, AkunFacebook, NamaPenerima) \
                    VALUES (%s, %s, %s, %s, %s, %s)", (6, "KITASABI", "@kitasabi", "@kitasabi", "kitasabi sabi sabi sabi bos", "RPL A DONG YA ALLAH AAMIIN"))

    # DUMMY LAMAN
    cursor.execute("INSERT INTO Laman (IDAutentikasi, IDPenggalang, Judul, Deskripsi, Target, Kategori, Deadline, Timestamp) \
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", (4, 1, "RPL A YA ALLAH AAMIIN", "iya kami butuh nilai makasihhh", 40000000, "Lainnya", "2022-04-20", "2022-04-10 00:00:00"))

    cursor.execute("INSERT INTO LamanFoto (IDLaman, Foto) \
                    VALUES (%s, %s)", (1, "https://media-exp1.licdn.com/dms/image/C5603AQEjN-E0Mq6B0Q/profile-displayphoto-shrink_400_400/0/1611977545705?e=1655942400&v=beta&t=AHNdJhzVTf_hgBRdoJce-bjYEgkSjVaGiw87M6qqlYQ"))

    cursor.execute("INSERT INTO Laman (IDAutentikasi, IDPenggalang, Judul, Deskripsi, Target, Kategori, Deadline, Timestamp) \
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", (1, 1, "LALALLA YEYEYEYE", "iya kami butuh nilai makasihhh", 1250000, "Kesehatan", "2022-04-20", "2022-04-10 00:00:00"))

    cursor.execute("INSERT INTO LamanFoto (IDLaman, Foto) \
                    VALUES (%s, %s)", (2, "https://kpopping.com/documents/c2/3/2000/210703-LOONA-Heejin-documents-1.jpeg"))

    cursor.execute("INSERT INTO Laman (IDAutentikasi, IDPenggalang, Judul, Deskripsi, Target, Kategori, Deadline, Timestamp) \
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", (2, 1, "WANGY WANGY HUHA HUHA", "iya kami butuh nilai makasihhh", 27000000, "Kesehatan", "2022-04-20", "2022-04-10 00:00:00"))

    cursor.execute("INSERT INTO LamanFoto (IDLaman, Foto) \
                    VALUES (%s, %s)", (3, "https://wiki.d-addicts.com/images/4/4c/IU.jpg"))

    # DUMMY TRANSAKSI
    cursor.execute("INSERT INTO Transaksi (IDDonatur, IDLaman, JumlahTransaksi, Timestamp) \
                    VALUES (%s, %s, %s, %s)", (1, 1, 6666, "2022-04-20 00:01:00"))

    cursor.execute("INSERT INTO Transaksi (IDDonatur, IDLaman, JumlahTransaksi, Timestamp) \
                    VALUES (%s, %s, %s, %s)", (1, 1, 7777, "2022-04-20 00:01:01"))

    cursor.execute("INSERT INTO Transaksi (IDDonatur, IDLaman, JumlahTransaksi, Timestamp) \
                    VALUES (%s, %s, %s, %s)", (1, 2, 8080, "2022-04-20 00:01:02"))

    cursor.execute("INSERT INTO Transaksi (IDDonatur, IDLaman, JumlahTransaksi, Timestamp) \
                    VALUES (%s, %s, %s, %s)", (1, 2, 2700, "2022-04-20 00:01:03"))

    cursor.execute("INSERT INTO Transaksi (IDDonatur, IDLaman, JumlahTransaksi, Timestamp) \
                    VALUES (%s, %s, %s, %s)", (1, 3, 1385, "2022-04-20 00:01:04"))

    cursor.execute("INSERT INTO Transaksi (IDDonatur, IDLaman, JumlahTransaksi, Timestamp) \
                    VALUES (%s, %s, %s, %s)", (1, 3, 1234, "2022-04-20 00:01:05"))
        

    mysql.connection.commit()
    cursor.close()