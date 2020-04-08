import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess' # for flask-wtf to protect web forms against a CSRF (seasurf)
