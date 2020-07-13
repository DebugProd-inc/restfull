from flask import url_for
from app import db


class ParameterValue(db.Model):
    __tablename__ = "parameter_values"
    id = db.Column(db.Integer, primary_key=True)
    id_parameter = db.Column(db.Integer, db.ForeignKey("parameters.id"))
    parameter = db.relationship("Parameter")
    time = db.Column(db.Time)
    value= db.Column(db.Float)
    id_flight = db.Column(db.Integer, db.ForeignKey("flights.id"))
    flight = db.relationship("Flight")