from app import db
from app.models.duration_of_phase import duration_of_phase


class PhaseOfFlight(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    flight = db.relationship(
        "Flight", secondary=duration_of_phase, back_populates="phase_of_flight"
    )
