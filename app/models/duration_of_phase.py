from app import db

# auxiliary table
duration_of_phase = db.Table(
    "duration_of_phase",
    db.Column("id_flight", db.Integer, db.ForeignKey("flight.id")),
    db.Column("id_phase", db.Integer, db.ForeignKey("phase_of_flight.id")),
    db.Column("start_phase", db.Time),
    db.Column("end_phase", db.Time)
    )
