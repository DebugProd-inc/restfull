from app import db


class Manufacturer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    model = db.relationship("Model")

    def __repr__(self):
        return f'<Manufacturer {self.name}>'
