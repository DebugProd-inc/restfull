from flask import url_for
from app import db


class Model(db.Model):
    __tablename__ = "models"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    id_manufacturer = db.Column(db.Integer, db.ForeignKey("manufacturers.id"))
    manufacturer = db.relationship("Manufacturer")
    boards = db.relationship("Board")


