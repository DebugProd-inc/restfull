from flask import url_for
from app import db
from app.models.utils.paginted_mixin import PaginatedAPIMixin


class Direction(PaginatedAPIMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    point_of_departure = db.Column(db.String)
    point_of_destination = db.Column(db.String)
    flight = db.relationship("Flight")

    def __repr__(self):
        return f'<Direction from {self.point_of_departure}>\
            to {self.point_of_destination}'

    def to_dict(self):
        data = {
            'id': self.id,
            'point_of_departure': self.point_of_departure,
            'point_of_destination': self.point_of_destination,
            '_links': {
                'self': url_for(
                    'api.get_direction',
                    id=self.id
                )
            }
        }
        return data

    def from_dict(self, data):
        for field in [
            'id',
            'point_of_departure',
            'point_of_destination'
        ]:
            if field in data:
                setattr(self, field, data[field])
