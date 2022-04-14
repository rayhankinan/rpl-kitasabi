from flask_mysqldb import MySQL

from config import databaseConfig
from application import app

app.config.from_object(databaseConfig)

mysql = MySQL(app)

# SETUP DDL
with app.app_context():
    cursor = mysql.connection.cursor()

    cursor.execute("DROP TABLE IF EXISTS Akun_No_Telp")
    cursor.execute("DROP TABLE IF EXISTS Akun")

    cursor.execute("CREATE TABLE Akun (IDPengguna INT UNSIGNED AUTO_INCREMENT, Email VARCHAR(320) UNIQUE NOT NULL, NamaDepan VARCHAR(255) NOT NULL, NamaBelakang VARCHAR(255) NOT NULL, Username VARCHAR(255) UNIQUE NOT NULL, Password VARBINARY(60) NOT NULL, Foto VARCHAR(255) DEFAULT NULL, PRIMARY KEY (IDPengguna))")
    cursor.execute("CREATE TABLE Akun_No_Telp (IDPengguna INT UNSIGNED, NoTelp VARCHAR(31), PRIMARY KEY (IDPengguna, NoTelp), FOREIGN KEY (IDPengguna) REFERENCES Akun (IDPengguna) ON DELETE CASCADE)")
    
    mysql.connection.commit()
    cursor.close()