from app import db


class Board(db.Model):
    registration_number = db.Column(db.String, primary_key=True)
    id_model = db.Column(db.Integer, db.ForeignKey("model.id"))
    model = db.relationship("Model")
    year_of_manufacture = db.Column(db.Integer)
    system = db.relationship("Subsystem")
    flight = db.relationship("Flight")

    def __repr__(self):
        return f'<Board {self.registration_number}>'
