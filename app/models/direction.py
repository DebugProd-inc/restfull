from app import db


class Direction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    point_of_departure = db.Column(db.String)
    point_of_destination = db.Column(db.String)
    flight = db.relationship("Flight")

    def __repr__(self):
        return f'<Direction from {self.point_of_departure}>\
            to {self.point_of_destination}'
