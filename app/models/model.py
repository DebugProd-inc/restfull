from app import db


class Model(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    id_manufacturer = db.Column(db.Integer, db.ForeignKey("manufacturer.id"))
    manufacturer = db.relationship("Manufacturer")
    board = db.relationship("Board")

    def __repr__(self):
        return f'<Model {self.name}>'
