#!/usr/bin/python3
from flask import Blueprint
from models import PrecinctResult


precinct_election_results_bp = Blueprint(
    'precinct_election_results', __name__)


precinct_election_results_bp.route(
    '/', methods=['GET'])(PrecinctResult.getList)
precinct_election_results_bp.route('/<int:resource_id>',
                                    methods=['GET'])(PrecinctResult.getOne)
