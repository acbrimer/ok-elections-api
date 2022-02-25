#!/usr/bin/python3
from .engine.app import db
from .base import BaseModel


class Precinct(db.Model, BaseModel):
    __tablename__ = 'precincts'

    id = db.Column(db.Integer, primary_key=True)
    ok_district_id = db.Column(db.Integer, nullable=False)
    precinct_num = db.Column(db.Integer, nullable=False)
    county_id = db.Column(db.Integer, db.ForeignKey('counties.id'), nullable=False)
    county_number = db.Column(db.Integer)
    ok_commissioner_district_id = db.Column(db.Integer)
    ok_house_district_id = db.Column(db.Integer)
    ok_senate_district_id = db.Column(db.Integer)
    us_congressional_district_id = db.Column(db.Integer)
    SHAPE_Area = db.Column(db.Integer, nullable=False)
    SHAPE_center_lat = db.Column(db.Float, nullable=False)
    SHAPE_center_lon = db.Column(db.Float, nullable=False)
