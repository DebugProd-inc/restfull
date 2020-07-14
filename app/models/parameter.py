from app import db


class Parameter(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, index=True)
    id_system = db.Column(db.Integer, db.ForeignKey("subsystem.id"))
    system = db.relationship("Subsystem")
    parameter_value = db.relationship("ParameterValue")

    def __repr__(self):
        return f'<Parameter {self.name}>'
