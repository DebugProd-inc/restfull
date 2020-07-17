from app import db
from app.models.duration_of_phase import duration_of_phase


class PhaseOfFlight(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    flight = db.relationship(
        "Flight", secondary=duration_of_phase, back_populates="phase_of_flight"
    )

    def __repr__(self):
        return f'<PhaseOfFlight {self.name}>'

    def to_dict(self):
        data = {
            'id': self.id,
            'name': self.name,
            '_links': {
                'self': url_for(
                    'api.get_phase_of_flight',
                    id=self.id
                )
            }
        }
        return data

    def from_dict(self, data):
        for field in [
            'id',
            'name'
        ]:
            if field in data:
                setattr(self, field, data[field])