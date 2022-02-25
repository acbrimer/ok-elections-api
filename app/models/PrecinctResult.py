#!/usr/bin/python3
from .engine.app import db
from .base import BaseModel


class PrecinctResult(db.Model, BaseModel):
    __tablename__ = 'precinct_results'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    precinct_id = db.Column(db.Integer, db.ForeignKey(
        "precincts.id"), nullable=False)
    election_race_id = db.Column(db.Integer, db.ForeignKey(
        "election_races.id"), nullable=False)
    precinct_tot_votes = db.Column(db.Integer, nullable=True)
    precinct_absmail_votes = db.Column(db.Integer, nullable=True)
    precinct_early_votes = db.Column(db.Integer, nullable=True)
    precinct_elecday_votes = db.Column(db.Integer, nullable=True)
    election_race_candidate_id = db.Column(
        db.Integer, db.ForeignKey('election_race_candidates.id'), nullable=False)
    cand_is_winner = db.Column(db.Boolean, nullable=False)
    cand_absmail_votes = db.Column(db.Integer, default=0, nullable=True)
    cand_early_votes = db.Column(db.Integer, default=0, nullable=True)
    cand_elecday_votes = db.Column(db.Integer, default=0, nullable=True)
    cand_tot_votes = db.Column(db.Integer, default=0, nullable=True)
