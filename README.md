# KITASABI
Disusun untuk memenuhi Tugas 7 Implementasi Perancangan Perangkat Lunak IF2250 Rekayasa Perangkat Lunak.

## Daftar Isi
* [Deskripsi Singkat Program](#deskripsi-singkat-program)
* [Struktur Program](#struktur-program)
* [Requirement Program](#requirement-program)
* [Cara Menyiapkan *Environment*](#cara-menyiapkan-environment)
* [Cara Menjalankan Program](#cara-menjalankan-program)
* [Cara Menggunakan Program](#cara-menggunakan-program)
* [Daftar Modul yang Diimplementasi](#daftar-modul-yang-diimplementasi)
* [Daftar Tabel Basis Data](#daftar-tabel-basis-data)
* [Author](#author)

## Deskripsi Singkat Program
User membutuhkan sebuah perangkat lunak yang diakses menggunakan desktop untuk melakukan penggalangan dana. Perangkat lunak ini dibuat sehingga perangkat lunak tersebut dapat diakses melalui desktop. <br/>

Awalnya seorang pengunjung mengakses perangkat lunak untuk menikmati layanan yang diberikan. Layanan yang diberikan adalah sebuah platform penggalangan dana. Pengunjung akan langsung diarahkan home page yang berisi daftar donasi yang dibuka. Pengunjung bisa melihat konten berupa tujuan penggalangan dana, foto, deskripsi singkat, tombol donasi untuk menyumbang dana, milestone dari penggalangan berupa target dana dan sisa waktu penggalangan dana, dan kolom pencarian untuk mencari penggalangan dana yang diinginkan berdasarkan masukan pengguna atau berdasarkan kategori. Untuk melihat deskripsi dengan lebih jelas, pengunjung bisa menekan konten tersebut lalu masuk ke halaman konten sebuah penggalangan dana tersebut. <br/>

Donasi yang dapat diterima berupa uang yang dapat dibayarkan melalui kredit atau debit yang dana tersebut akan masuk ke rekening perusahaan pengelola perangkat lunak, yang nantinya akan diberikan kepada penggalang dana apabila memenuhi verifikasi data yang dibutuhkan untuk pencairan dana. Pengunjung juga dapat membuat penggalangan dana sendiri. <br/>

Untuk melakukan penggalangan dana ataupun melakukan donasi, pengunjung diwajibkan untuk melakukan login, apabila pengunjung belum memiliki akun, pengunjung bisa mendaftar terlebih dahulu dan melakukan verifikasi data diri seperti rekening debit atau kredit. P/L desktop ini akan berkomunikasi menggunakan server untuk memproses permintaan dari pengunjung yang melakukan transaksi ke database yang ada. <br/>

## Struktur Program
```bash
.
│   .gitignore
│   .gitlab-ci.yml
│   README.md
│   requirements.txt
│   
└───src
    │   .gitignore
    │   application.py
    │   main.py
    │   
    ├───controllers
    │       akunControllers.py
    │       lamanControllers.py
    │       permintaanControllers.py
    │       transaksiControllers.py
    │       
    ├───models
    │       akunModels.py
    │       cdn.py
    │       db.py
    │       lamanModels.py
    │       permintaanModels.py
    │       transaksiModels.py
    │       
    ├───routes
    │       akunRoutes.py
    │       lamanRoutes.py
    │       permintaanRoutes.py
    │       transaksiRoutes.py
    │       
    └───views
            custom_widgets.py
            formKesehatan.py
            formLogin.py
            formNonKesehatan.py
            formRegister.py
            lamanDetail.py
            lamanEksplor.py
            lamanPembayaran.py
            lamanPengelolaanAkun.py
            lamanPenggalangDana.py
            lamanPermintaan.py
            lamanRiwayatDonasi.py
            lamanRiwayatPenggalanganDana.py
            mainWindow.py
            pageBuilder.py
            pageController.py
```

## Requirement Program
* Python versi 3.7.6 atau lebih baru. Pastikan pula terdapat package PyPi (PIP) pada Python Anda.
* Google Gloud SDK versi 380.0.0 atau lebih baru.
* MySQL versi 8.0.26 atau lebih baru.

## Cara Menyiapkan *Environment*
1. Pastikan seluruh requirement program sudah terpasang pada komputer (Anda dapat mengecek versi Python dengan menjalankan *command* `py --version` pada *command prompt*).
2. Lakukan instalasi semua *library* yang digunakan pada program. Anda dapat menginstalasi seluruh *library* yang digunakan pada program ini dengan menjalankan *command* `pip install -r requirements.txt` pada *command prompt*.
3. Jika seluruh *library* berhasil diinstalasi, maka akan terdapat pemberitahuan pada *command prompt*.
4. Pastikan pula Google Cloud SDK sudah terpasang pada komputer (Anda dapat menginisialisasi Google Cloud SDK dengan menjalankan *command* `gcloud init` pada *command prompt*).
5. Tambahkan *database* baru pada DBMS MySQL bernama `KITASABI`.

## Cara Menjalankan Program
1. Pastikan sudah menyiapkan *environment* program serta komputer terhubung dengan internet.
2. Jalankan program `main.py` dengan menjalankan perintah `py src/main.py` pada *command prompt*.
3. Jika berhasil dijalankan, maka akan terdapat *window* Python pada komputer.

## Daftar Modul yang Diimplementasi

## Daftar Tabel Basis Data
* Tabel Akun
```
+--------------+---------------+------+-----+---------+----------------+
| Field        | Type          | Null | Key | Default | Extra          |
+--------------+---------------+------+-----+---------+----------------+
| IDPengguna   | int unsigned  | NO   | PRI | NULL    | auto_increment |
| Email        | varchar(320)  | NO   | UNI | NULL    |                |
| NamaDepan    | varchar(255)  | NO   |     | NULL    |                |
| NamaBelakang | varchar(255)  | NO   |     | NULL    |                |
| Username     | varchar(255)  | NO   | UNI | NULL    |                |
| Password     | varbinary(60) | NO   |     | NULL    |                |
| Foto         | varchar(255)  | NO   |     | NULL    |                |
+--------------+---------------+------+-----+---------+----------------+
```

* Tabel AkunNoTelp
```
+------------+--------------+------+-----+---------+-------+
| Field      | Type         | Null | Key | Default | Extra |
+------------+--------------+------+-----+---------+-------+
| IDPengguna | int unsigned | NO   | PRI | NULL    |       |
| NoTelp     | varchar(31)  | NO   | PRI | NULL    |       |
+------------+--------------+------+-----+---------+-------+
```

* Tabel Permintaan
```
+-------------------+-----------------+------+-----+---------+----------------+
| Field             | Type            | Null | Key | Default | Extra          |
+-------------------+-----------------+------+-----+---------+----------------+
| IDPermintaan      | int unsigned    | NO   | PRI | NULL    | auto_increment |
| IDPengguna        | int unsigned    | NO   | MUL | NULL    |                |
| Judul             | varchar(255)    | NO   | MUL | NULL    |                |
| Deskripsi         | varchar(255)    | NO   |     | NULL    |                |
| Target            | bigint unsigned | NO   |     | NULL    |                |
| StatusAutentikasi | tinyint(1)      | YES  |     | NULL    |                |
+-------------------+-----------------+------+-----+---------+----------------+
```

* Tabel Permintaan Kesehatan
```
+--------------------------+--------------+------+-----+---------+-------+
| Field                    | Type         | Null | Key | Default | Extra |
+--------------------------+--------------+------+-----+---------+-------+
| IDPermintaanKesehatan    | int unsigned | NO   | PRI | NULL    |       |
| FotoKTP                  | varchar(255) | NO   |     | NULL    |       |
| FotoKK                   | varchar(255) | NO   |     | NULL    |       |
| FotoSuratKeteranganMedis | varchar(255) | NO   |     | NULL    |       |
| FotoHasilPemeriksaan     | varchar(255) | NO   |     | NULL    |       |
| Tujuan                   | varchar(255) | NO   |     | NULL    |       |
| NamaPasien               | varchar(255) | NO   |     | NULL    |       |
+--------------------------+--------------+------+-----+---------+-------+
```

* Tabel Permintaan Lainnya
```
+---------------------+--------------+------+-----+---------+-------+
| Field               | Type         | Null | Key | Default | Extra |
+---------------------+--------------+------+-----+---------+-------+
| IDPermintaanLainnya | int unsigned | NO   | PRI | NULL    |       |
| Instansi            | varchar(255) | NO   |     | NULL    |       |
| AkunInstagram       | varchar(255) | YES  |     | NULL    |       |
| AkunTwitter         | varchar(255) | YES  |     | NULL    |       |
| AkunFacebook        | varchar(255) | YES  |     | NULL    |       |
| NamaPenerima        | varchar(255) | NO   |     | NULL    |       |
+---------------------+--------------+------+-----+---------+-------+
```

* Tabel Laman
```
+---------------+-----------------------------+------+-----+---------+----------------+
| Field         | Type                        | Null | Key | Default | Extra          |
+---------------+-----------------------------+------+-----+---------+----------------+
| IDLaman       | int unsigned                | NO   | PRI | NULL    | auto_increment |
| IDAutentikasi | int unsigned                | NO   | MUL | NULL    |                |
| IDPenggalang  | int unsigned                | NO   | MUL | NULL    |                |
| Judul         | varchar(255)                | NO   |     | NULL    |                |
| Deskripsi     | varchar(255)                | NO   |     | NULL    |                |
| Target        | bigint unsigned             | NO   |     | NULL    |                |
| Kategori      | enum('Kesehatan','Lainnya') | NO   |     | NULL    |                |
| Deadline      | date                        | NO   |     | NULL    |                |
| Timestamp     | datetime                    | NO   |     | NULL    |                |
+---------------+-----------------------------+------+-----+---------+----------------+
```

* Tabel Laman Foto
```
+---------+--------------+------+-----+---------+-------+
| Field   | Type         | Null | Key | Default | Extra |
+---------+--------------+------+-----+---------+-------+
| IDLaman | int unsigned | NO   | PRI | NULL    |       |
| Foto    | varchar(255) | NO   | PRI | NULL    |       |
+---------+--------------+------+-----+---------+-------+
```

* Tabel Transaksi
```
+-----------------+-----------------+------+-----+-------------------+-------------------+
| Field           | Type            | Null | Key | Default           | Extra             |
+-----------------+-----------------+------+-----+-------------------+-------------------+
| IDTransaksi     | int unsigned    | NO   | PRI | NULL              | auto_increment    |
| IDDonatur       | int unsigned    | YES  | MUL | NULL              |                   |
| IDLaman         | int unsigned    | YES  | MUL | NULL              |                   |
| JumlahTransaksi | bigint unsigned | NO   |     | NULL              |                   |
| Timestamp       | timestamp       | NO   |     | CURRENT_TIMESTAMP | DEFAULT_GENERATED |
| StatusPencairan | tinyint(1)      | NO   |     | 0                 |                   |
+-----------------+-----------------+------+-----+-------------------+-------------------+
```

## Author
* [Adiyansa Prasetya Wicaksana - 13520044](https://gitlab.informatika.org/apwic)
* [Fikri Khoiron Fadhila - 13520056](https://gitlab.informatika.org/fikrikhoironn)
* [Rayhan Kinan Muhannad - 13520065](https://gitlab.informatika.org/rayhankinan)
* [Sarah Azka - 13520083](https://gitlab.informatika.org/sarahzka)