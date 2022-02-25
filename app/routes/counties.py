#!/usr/bin/python3
from flask import Blueprint
from models import County


counties_bp = Blueprint('counties', __name__)


counties_bp.route('/', methods=['GET'])(County.getList)
counties_bp.route('/<int:resource_id>',
                  methods=['GET'])(County.getOne)
