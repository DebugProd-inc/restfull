from app import db


class Subsystem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    id_board = db.Column(
        db.Integer,
        db.ForeignKey("board.registration_number")
    )
    board = db.relationship("Board")
    parameter = db.relationship("Parameter")
