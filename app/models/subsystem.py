from app import db


class Subsystem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, index=True)
    id_board = db.Column(
        db.Integer,
        db.ForeignKey("board.registration_number")
    )
    board = db.relationship("Board")
    parameter = db.relationship("Parameter")

    def __repr__(self):
        return f'<Subsystem {self.name}>'
