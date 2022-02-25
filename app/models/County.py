#!/usr/bin/python3
from .engine.app import db
from .base import BaseModel


class County(db.Model, BaseModel):
    __tablename__ = 'counties'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=True)
    state_id = db.Column(db.Integer, db.ForeignKey(
        'states.id'), nullable=False)
    SHAPE_Area = db.Column(db.Integer, nullable=False)
    SHAPE_center_lat = db.Column(db.Float, nullable=False)
    SHAPE_center_lon = db.Column(db.Float, nullable=False)
