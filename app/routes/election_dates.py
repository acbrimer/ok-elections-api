#!/usr/bin/python3
from flask import Blueprint
from models import ElectionDate
from flask_cors import CORS


election_dates_bp = Blueprint('election_dates', __name__)


election_dates_bp.route('/', methods=['GET'])(ElectionDate.getList)
election_dates_bp.route('/<int:resource_id>',
                        methods=['GET'])(ElectionDate.getOne)
