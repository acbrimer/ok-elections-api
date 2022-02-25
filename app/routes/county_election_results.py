#!/usr/bin/python3
from flask import Blueprint
from models import CountyElectionResult

county_election_results_bp = Blueprint('county_election_results', __name__)

county_election_results_bp.route(
    '/', methods=['GET'])(CountyElectionResult.getList)
county_election_results_bp.route('/<int:resource_id>',
                                 methods=['GET'])(CountyElectionResult.getOne)
