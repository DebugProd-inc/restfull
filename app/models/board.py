from flask import url_for
from app import db
from app.models.utils.paginted_mixin import PaginatedAPIMixin


class Board(PaginatedAPIMixin, db.Model):
    registration_number = db.Column(db.String, primary_key=True)
    id_model = db.Column(db.Integer, db.ForeignKey("model.id"))
    model = db.relationship("Model")
    year_of_manufacture = db.Column(db.Integer)
    subsystem = db.relationship("Subsystem")
    flight = db.relationship("Flight")

    def __repr__(self):
        return f'<Board {self.registration_number}>'

    def to_dict(self):
        data = {
            'registration_number': self.registration_number,
            'id_model': self.id_model,
            'year_of_manufacture': self.year_of_manufacture,
            '_links': {
                'self': url_for(
                    'api.get_board',
                    registration_number=self.registration_number)
            }
        }
        return data

    def from_dict(self, data):
        for field in [
            'registration_number',
            'id_model',
            'year_of_manufacture'
        ]:
            if field in data:
                setattr(self, field, data[field])
