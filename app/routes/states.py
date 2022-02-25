#!/usr/bin/python3
from flask import Blueprint
from models import State


states_bp = Blueprint('states', __name__)


states_bp.route('/', methods=['GET'])(State.getList)
states_bp.route('/<int:resource_id>',
                methods=['GET'])(State.getOne)
