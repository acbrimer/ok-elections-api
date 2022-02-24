#!/usr/bin/python3
from sqlalchemy import ForeignKey
from .engine.app import db
from .base import BaseModel


class ElectionRace(db.Model, BaseModel):
    __tablename__ = 'election_races'
    DEFAULT_SORT = 'race_tot_votes'
    DEFAULT_ORDER = 'DEC'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    race_number = db.Column(db.String(255), nullable=True)
    elec_date_id = db.Column(db.Integer, ForeignKey("election_dates.id"))
    elec_date = db.Column(db.Date, nullable=False)
    race_description = db.Column(db.String(255), nullable=True)
    race_party = db.Column(db.String(255), nullable=True)
    tot_race_prec = db.Column(db.Integer, nullable=True)
    race_prec_reporting = db.Column(db.Integer, nullable=True, default=0)
    race_tot_votes = db.Column(db.Integer, nullable=True)
    race_absmail_votes = db.Column(db.Integer, nullable=True)
    race_early_votes = db.Column(db.Integer, nullable=True)
    race_elecday_votes = db.Column(db.Integer, nullable=True)
    race_num_candidates = db.Column(db.Integer, nullable=True)
