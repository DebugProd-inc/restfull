from flask import url_for
from app import db


class Manufacturer(db.Model):
    __tablename__ = "manufacturers"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    models = db.relationship("Model")