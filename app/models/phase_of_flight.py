from flask import url_for
from app import db


class PhaseOfFlight(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    flight = db.relationship(
        "Flight",secondary=duration_of_phase, back_populates="phase_of_flight"
    )