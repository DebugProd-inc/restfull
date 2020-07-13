from app import db


class Flight(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_board = db.Column(db.Integer, db.ForeignKey("board.id"))
    board = db.relationship("Board")
    id_direction = db.Column(db.Integer, db.ForeignKey("direction.id"))
    direction = db.relationship("Direction")
    time_begin = db.Column(db.Time)
    data_begin = db.Column(db.Data)
    phase_of_flight = db.relationship(
        "PhaseOfFlight", secondary=duration_of_phase, back_populates="flight"
    )
    parameter_value = db.relationship("ParameterValue")
