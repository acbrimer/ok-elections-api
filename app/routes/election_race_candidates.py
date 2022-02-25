#!/usr/bin/python3
from flask import Blueprint
from models import ElectionRaceCandidate

election_race_candidates_bp = Blueprint('election_race_candidates', __name__)

election_race_candidates_bp.route(
    '/', methods=['GET'])(ElectionRaceCandidate.getList)
election_race_candidates_bp.route('/<int:resource_id>',
                                 methods=['GET'])(ElectionRaceCandidate.getOne)
