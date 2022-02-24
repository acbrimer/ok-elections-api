#!/usr/bin/python3
"""Init views"""
from models.engine.app import app
from .election_dates import election_dates_bp
from .election_races import election_race_bp


app.register_blueprint(election_dates_bp, url_prefix='/election_dates')
app.register_blueprint(election_race_bp, url_prefix='/election_races')
