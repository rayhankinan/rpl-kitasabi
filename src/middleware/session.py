from flask_session import Session

from config import sessionConfig
from application import app

app.config.from_object(sessionConfig)

sess = Session(app)