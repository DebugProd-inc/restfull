from flask import url_for
from app import db
from app.models.duration_of_phase import duration_of_phase


class Flight(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_board = db.Column(
        db.String,
        db.ForeignKey("board.registration_number")
    )
    board = db.relationship("Board")
    id_direction = db.Column(db.Integer, db.ForeignKey("direction.id"))
    direction = db.relationship("Direction")
    time_begin = db.Column(db.Time)
    date_begin = db.Column(db.Date)
    phase_of_flight = db.relationship(
        "PhaseOfFlight", secondary=duration_of_phase, back_populates="flight"
    )
    parameter_value = db.relationship("ParameterValue")  # Тут это точно нужно?

    def __repr__(self):
        return f'<Flight {self.id} of id_board {self.id_board}>'

    def to_dict(self):
        data = {
            'id': self.id,
            'id_board': self.id_board,
            'id_direction': self.id_direction,
            'time_begin': self.time_begin,
            'date_begin': self.date_begin,
            '_links': {
                'self': url_for(
                    'api.get_flight',
                    id=self.id
                )
            }
        }
        return data

    def from_dict(self, data):
        for field in [
            'id',
            'id_board',
            'id_direction',
            'time_begin',
            'date_begin'
        ]:
            if field in data:
                setattr(self, field, data[field])
