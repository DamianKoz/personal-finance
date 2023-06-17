import os
from dotenv import load_dotenv

load_dotenv()


class Config(object):
    SECRET_KEY = os.environ.get("SECRET_KEY") or "you-will-never-guess"
    FLASK_APP = os.environ.get("FLASK_APP")
    FLASK_ENV = os.environ.get("FLASK_ENV")
    DEBUG = True if FLASK_ENV == "development" else False
    SQLALCHEMY_DATABASE_URI = "sqlite:///database.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False