from flask import url_for
from app import db


class Parameter(db.Model):
    __tablename__ = "Parameters"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    
