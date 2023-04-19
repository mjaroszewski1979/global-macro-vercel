from os import environ

SECRET_KEY = environ.get('SECRET_KEY')
SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'
SQLALCHEMY_TRACK_MODIFICATIONS = False