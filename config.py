import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess' # for flask-wtf to protect web forms against a CSRF (seasurf)

    SQLALCHEMY_DATABSE_URI = os.environ.get('DATABSE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db') # location of the app's SQLite database
    SQLALCHEMY_TRACK_MODIFICATIONS = False # do not signal the app every time a change is about to be made in the database