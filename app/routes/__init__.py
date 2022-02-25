#!/usr/bin/python3
"""Init views"""
from models.engine.app import app
from .election_dates import election_dates_bp
from .election_races import election_race_bp
from .states import states_bp
from .counties import counties_bp
from .precincts import precincts_bp
from .county_election_results import county_election_results_bp
from .election_race_candidates import election_race_candidates_bp
from .precinct_election_results import precinct_election_results_bp

app.register_blueprint(election_dates_bp, url_prefix='/election_dates')
app.register_blueprint(election_race_bp, url_prefix='/election_races')
app.register_blueprint(election_race_candidates_bp,
                       url_prefix='/election_race_candidates')
app.register_blueprint(states_bp, url_prefix='/states')
app.register_blueprint(counties_bp, url_prefix='/counties')
app.register_blueprint(precincts_bp, url_prefix='/precincts')
app.register_blueprint(county_election_results_bp,
                       url_prefix='/county_election_results')
app.register_blueprint(precinct_election_results_bp,
                       url_prefix='/precinct_election_results')
