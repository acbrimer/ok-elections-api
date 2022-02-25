#!/usr/bin/python3
from .engine.app import db
from .base import BaseModel


class ElectionRaceCandidate(db.Model, BaseModel):
    __tablename__ = 'election_race_candidates'

    id = db.Column(db.Integer, primary_key=True)
    election_race_id = db.Column(db.Integer, db.ForeignKey('election_races.id'),
                                 nullable=False)

    cand_number = db.Column(db.SmallInteger, nullable=False)
    cand_name = db.Column(db.String(500), nullable=False)
    cand_party = db.Column(db.String(10), nullable=True)
    cand_is_winner = db.Column(db.Boolean, nullable=False)
    cand_absmail_votes = db.Column(db.Integer, default=0, nullable=True)
    cand_early_votes = db.Column(db.Integer, default=0, nullable=True)
    cand_elecday_votes = db.Column(db.Integer, default=0, nullable=True)
    cand_tot_votes = db.Column(db.Integer, default=0, nullable=True)
    percent_tot_votes = db.Column(db.Float, default=0, nullable=True)
    percent_absmail_votes = db.Column(db.Float, default=0, nullable=True)
    percent_elecday_votes = db.Column(db.Float, default=0, nullable=True)
    percent_early_votes = db.Column(db.Float, default=0, nullable=True)
