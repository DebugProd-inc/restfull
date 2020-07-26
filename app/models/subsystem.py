from app import db


class Subsystem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, index=True)
    id_board = db.Column(
        db.Integer,
        db.ForeignKey("board.registration_number")
    )
    board = db.relationship("Board")
    parameter = db.relationship("Parameter")

    def __repr__(self):
        return f'<Subsystem {self.name}>'

    def to_dict(self):
        data = {
            'id': self.id,
            'name': self.name,
            'id_board': self.id_board,
            '_links': {
                'self': url_for(
                    'api.get_subsystem',
                    id=self.id
                )
            }
        }
        return data

    def from_dict(self, data):
        for field in [
            'id',
            'name',
            'id_board'
        ]:
            if field in data:
                setattr(self, field, data[field])