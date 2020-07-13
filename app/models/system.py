from flask import url_for
from app import db


class System(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    id_board = db.Column(db.Integer, db.ForeignKey("board.id"))
    board = db.relationship("Board")
    parameter = db.relationship("Parameter")