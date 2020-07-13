from flask import url_for
from app import db


class Flight(db.Model):
    __tablename__ = "flights"
    id = db.Column(db.Integer, primary_key=True)
    id_board = db.Column(db.Integer, db.ForeignKey("boards.id"))
    board = db.relationship("Board")
    id_direction = db.Column(db.Integer, db.ForeignKey("directions.id"))
    direction = db.relationship("Direction")
    time_begin = db.Column(db.Time)
    data_begin = db.Column(db.Data)
    phases_of_flight = db.relationship(
        "PhaseOfFlight", secondary=duration_of_phase, back_populates="flights"
    )
    parameter_values = db.relationship("ParameterValue")