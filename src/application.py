from flask import Flask
from flask_session import Session
from config import applicationConfig

app = Flask(__name__)
app.config.from_object(applicationConfig)

Session(app)