from flask import Flask
from config import applicationConfig

app = Flask(__name__)
app.config.from_object(applicationConfig)