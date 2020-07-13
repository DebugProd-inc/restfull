from app import db


class ParameterValue(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_parameter = db.Column(db.Integer, db.ForeignKey("parameter.id"))
    parameter = db.relationship("Parameter")
    time = db.Column(db.Time)
    value = db.Column(db.Float)
    id_flight = db.Column(db.Integer, db.ForeignKey("flight.id"))
    flight = db.relationship("Flight")
