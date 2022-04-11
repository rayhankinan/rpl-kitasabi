from flask_mysqldb import MySQL
from config import databaseConfig
from application import app

app.config.from_object(databaseConfig)

mysql = MySQL(app)