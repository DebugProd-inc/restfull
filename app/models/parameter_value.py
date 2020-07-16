from app import db


class ParameterValue(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_parameter = db.Column(db.Integer, db.ForeignKey("parameter.id"))
    parameter = db.relationship("Parameter")
    time = db.Column(db.Time, index=True)
    value = db.Column(db.Float, index=True)
    id_flight = db.Column(db.Integer, db.ForeignKey("flight.id"))
    flight = db.relationship("Flight")

    def __repr__(self):
        return f'<ParameterValue {self.value} \
            of id_parameter {self.id_parameter}>'

     def to_dict(self):
        data = {
            'id': self.id,
            'id_parameter': self.id_parameter,
            'time': self.time,
            'value': self.value,
            'id_flight': self.id_flight,
            '_links': {
                'self': url_for(
                    'api.get_parameter_value',
                    id=self.id
                )
            }
        }
        return data

    def from_dict(self, data):
        for field in [
            'id',
            'id_parameter',
            'time',
            'value',
            'id_flight'
        ]:
            if field in data:
                setattr(self, field, data[field])           
