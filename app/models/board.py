from flask import url_for
from app import db


class Board(db.Model):
    registration_number = db.Column(db.String, primary_key=True) 
    id_model = db.Column(db.Integer, db.ForeignKey("model.id"))
    model = db.relationship("Model")
    year_of_manufacture = db.Column(db.Integer)
    system = db.relationship("System")
    flight = db.relationship("Flight")