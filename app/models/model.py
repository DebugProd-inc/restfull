from flask import url_for
from app import db


class Model(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    id_manufacturer = db.Column(db.Integer, db.ForeignKey("manufacturer.id"))
    manufacturer = db.relationship("Manufacturer")
    board = db.relationship("Board")

    def __repr__(self):
        return f'<Model {self.name}>'

    def to_dict(self):
        data = {
            'id': self.id,
            'name': self.name,
            'id_manufacturer': self.id_manufacturer,
            '_links': {
                'self': url_for(
                    'api.get_model',
                    id=self.id
                )
            }
        }
        return data

    def from_dict(self, data):
        for field in [
            'id',
            'name',
            'id_manufacturer'
        ]:
            if field in data:
                setattr(self, field, data[field])
