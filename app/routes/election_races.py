#!/usr/bin/python3
from flask import Blueprint
from models import ElectionRace

election_race_bp = Blueprint('election_races', __name__)

election_race_bp.route('/', methods=['GET'])(ElectionRace.getList)
election_race_bp.route('/<int:resource_id>',
                       methods=['GET'])(ElectionRace.getOne)
