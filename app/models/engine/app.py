import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Set up the SQLAlchemy Database to be a local file 'app.db'

dbPath = os.path.join(os.path.dirname(
    os.path.realpath(__file__)), '../../app.db')

app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{dbPath}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# ^ Cloud Run logs said I should set this option to false
db = SQLAlchemy(app)
