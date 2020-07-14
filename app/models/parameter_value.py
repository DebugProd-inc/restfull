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
