from flask import url_for
from app import db


class Direction(db.Model):
    __tablename__ = "directions"
    id = db.Column(db.Integer, primary_key=True)
    point_of_departure = db.Column(db.String)
    point_of_destination = db.Column(db.String)
    flights = db.relationship("Flight")