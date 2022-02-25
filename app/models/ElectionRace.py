#!/usr/bin/python3
from .engine.app import db
from .base import BaseModel


class ElectionRace(db.Model, BaseModel):
    __tablename__ = 'election_races'
    DEFAULT_SORT = ['race_tot_votes', 'DESC']

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    race_number = db.Column(db.String(255), nullable=True)
    elec_date_id = db.Column(db.Integer, db.ForeignKey("election_dates.id"))
    race_county_owner = db.Column(db.String(255), nullable=True)
    elec_date = db.Column(db.Date, nullable=False)
    race_entity_description = db.Column(db.String(255), nullable=True)
    race_description = db.Column(db.String(255), nullable=True)
    race_party = db.Column(db.String(255), nullable=True)
    race_tot_prec = db.Column(db.Integer, nullable=True)
    race_prec_reporting = db.Column(db.Integer, nullable=True, default=0)
    race_tot_votes = db.Column(db.Integer, nullable=True)
    race_absmail_votes = db.Column(db.Integer, nullable=True)
    race_early_votes = db.Column(db.Integer, nullable=True)
    race_elecday_votes = db.Column(db.Integer, nullable=True)
    race_num_candidates = db.Column(db.Integer, nullable=True)

    candidate_results = db.relationship(
        'ElectionRaceCandidate', lazy="dynamic")

    def toDict(self):
        d = BaseModel.toDict(self)
        d['candidate_results'] = [cr.toDict() for cr in self.candidate_results]
        return d
