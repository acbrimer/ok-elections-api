#!/usr/bin/python3
from .engine.app import db
from .base import BaseModel


class PrecinctElectionCandidateResult(db.Model, BaseModel):
    __tablename__ = 'precinct_election_candidate_results'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    precinct_election_result_id = db.Column(
        db.Integer, db.ForeignKey("precinct_election_results.id"))
    election_race_candidate_id = db.Column(
        db.Integer, db.ForeignKey('election_race_candidates.id'), nullable=False)
    cand_is_winner = db.Column(db.Boolean, nullable=False)
    cand_absmail_votes = db.Column(db.Integer, default=0, nullable=True)
    cand_early_votes = db.Column(db.Integer, default=0, nullable=True)
    cand_elecday_votes = db.Column(db.Integer, default=0, nullable=True)
    cand_tot_votes = db.Column(db.Integer, default=0, nullable=True)
    percent_tot_votes = db.Column(db.Float, default=0, nullable=True)
    percent_absmail_votes = db.Column(db.Float, default=0, nullable=True)
    percent_elecday_votes = db.Column(db.Float, default=0, nullable=True)
    percent_early_votes = db.Column(db.Float, default=0, nullable=True)
