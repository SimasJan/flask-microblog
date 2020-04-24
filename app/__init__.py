import os
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config.from_object(Config)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
app.config['SQLALCHEMY_DATABSE_URI'] = os.environ.get('DATABSE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db') # location of the app's SQLite database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
# do not signal the app every time a change is about to be made in the database

db = SQLAlchemy()
db.init_app(app)

migrate = Migrate(app, db) #migration engine

from app import routes, models