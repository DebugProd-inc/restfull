from flask import url_for
from app import db


class Board(db.Model):
    __tablename__ = "boards"
    registration_number = db.Column(db.Integer, primary_key=True) #значение полей состоит из латинских букв по идее, не знаю, где пока искать его 
    id_model = db.Column(db.Integer, db.ForeignKey("models.id"))
    model = db.relationship("Model")
    year_of_manufacture = db.Column(db.Integer)