#!/usr/bin/python3
from flask import Blueprint
from models import Precinct


precincts_bp = Blueprint('precincts', __name__)


precincts_bp.route('/', methods=['GET'])(Precinct.getList)
precincts_bp.route('/<int:resource_id>',
                        methods=['GET'])(Precinct.getOne)
