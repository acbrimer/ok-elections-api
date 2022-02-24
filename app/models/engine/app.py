import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Set up the SQLAlchemy Database to be a local file 'desserts.db'

dbPath = os.path.join(os.path.dirname(
    os.path.realpath(__file__)), '../../app.db')

app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{dbPath}'
db = SQLAlchemy(app)
