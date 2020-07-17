from app import db


class Parameter(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, index=True)
    id_system = db.Column(db.Integer, db.ForeignKey("subsystem.id"))
    system = db.relationship("Subsystem")
    parameter_value = db.relationship("ParameterValue")

    def __repr__(self):
        return f'<Parameter {self.name}>'

    def to_dict(self):
        data = {
            'id': self.id,
            'name': self.name,
            'id_system': self.id_system,
            '_links': {
                'self': url_for(
                    'api.get_parameter',
                    id=self.id
                )
            }
        }
        return data

    def from_dict(self, data):
        for field in [
            'id',
            'name',
            'id_system'
        ]:
            if field in data:
                setattr(self, field, data[field])