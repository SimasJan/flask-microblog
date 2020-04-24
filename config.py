import os

basedir = os.path.abspath(os.path.dirname(__file__))

class BaseConfig(object):
    DEBUG = False
        
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess' # for flask-wtf to protect web forms against a CSRF (seasurf)
    # location of the app's SQLite database
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    # do not signal the app every time a change is about to be made in the database
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class TestingConfig(BaseConfig):
    DEBUG = False
    TESTING = True
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + 'your_test_db_name_file'