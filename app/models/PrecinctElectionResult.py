#!/usr/bin/python3
from .engine.app import db
from .base import BaseModel


class PrecinctElectionResult(db.Model, BaseModel):
    __tablename__ = 'precinct_election_results'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    precinct_id = db.Column(db.Integer, db.ForeignKey(
        "precincts.id"), nullable=False)
    election_race_id = db.Column(db.Integer, db.ForeignKey(
        "election_races.id"), nullable=False)
    precinct_tot_votes = db.Column(db.Integer, nullable=True)
    precinct_absmail_votes = db.Column(db.Integer, nullable=True)
    precinct_early_votes = db.Column(db.Integer, nullable=True)
    precinct_elecday_votes = db.Column(db.Integer, nullable=True)


    # def toDict(self):
    #     d = BaseModel.toDict(self)
    #     d['candidate_results'] = [cr.toDict() for cr in self.candidate_results]
    #     return d
