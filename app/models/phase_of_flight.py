from flask import url_for
from app import db


class PhaseOfFlight(db.Model):
    __tablename__ = "phases_of_flight"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    flights = db.relationship(
        "Flight",secondary=duration_of_phase, back_populates="phases_of_flight"
    )