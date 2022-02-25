#!/usr/bin/python3
from .engine.app import db
from .base import BaseModel


class State(db.Model, BaseModel):
    __tablename__ = 'states'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    postal_code = db.Column(db.CHAR(2), nullable=False)
