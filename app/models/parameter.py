from flask import url_for
from app import db


class Parameter(db.Model):
    __tablename__ = "parameters"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    id_system = db.Column(db.Integer, db.ForeignKey("systems.id"))
    system = db.relationship("System")
    parameter_values = db.relationship("ParameterValue")