#!/usr/bin/python3
from .engine.app import db
from .base import BaseModel


class CountyElectionResult(db.Model, BaseModel):
    __tablename__ = 'county_election_results'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    county_id = db.Column(db.Integer, db.ForeignKey(
        "counties.id"), nullable=False)
    election_race_id = db.Column(db.Integer, db.ForeignKey(
        "election_races.id"), nullable=False)
    county_tot_prec = db.Column(db.Integer, nullable=True)
    county_prec_reporting = db.Column(db.Integer, nullable=True, default=0)
    county_tot_votes = db.Column(db.Integer, nullable=True)
    county_absmail_votes = db.Column(db.Integer, nullable=True)
    county_early_votes = db.Column(db.Integer, nullable=True)
    county_elecday_votes = db.Column(db.Integer, nullable=True)
    percent_tot_votes = db.Column(db.Integer, nullable=True)
    percent_absmail_votes = db.Column(db.Integer, nullable=True)
    percent_early_votes = db.Column(db.Integer, nullable=True)
    percent_elecday_votes = db.Column(db.Integer, nullable=True)

    candidate_results = db.relationship(
        'CountyElectionCandidateResult', lazy="dynamic")

    def toDict(self):
        d = BaseModel.toDict(self)
        d['candidate_results'] = [cr.toDict() for cr in self.candidate_results]
        return d
