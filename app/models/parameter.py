from flask import url_for
from app import db


class Parameter(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    id_system = db.Column(db.Integer, db.ForeignKey("system.id"))
    system = db.relationship("System")
    parameter_value = db.relationship("ParameterValue")