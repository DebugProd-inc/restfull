from flask import url_for
from app import db


class Manufacturer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    model = db.relationship("Model")

    def __repr__(self):
        return f'<Manufacturer {self.name}>'

    def to_dict(self):
        data = {
            'id': self.id,
            'name': self.name,
            '_links': {
                'self': url_for(
                    'api.get_manufacturer',
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
