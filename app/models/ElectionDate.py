#!/usr/bin/python3
from .engine.app import db
from .base import BaseModel


class ElectionDate(db.Model, BaseModel):
    __tablename__ = 'election_dates'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, unique=True, nullable=False)
    label = db.Column(db.String(255), nullable=True)
