from flask import url_for
from app import db


class System(db.Model):
    __tablename__ = "systems"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    id_board = db.Column(db.Integer, db.ForeignKey("boards.id"))
    board = db.relationship("Board")
    parameters = db.relationship("Parameter")