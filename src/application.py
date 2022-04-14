from flask import Flask
from dotenv import load_dotenv

from config import applicationConfig

load_dotenv()

app = Flask(__name__)
app.config.from_object(applicationConfig)