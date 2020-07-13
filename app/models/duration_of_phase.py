from flask import url_for
from app import db


duration_of_phase = db.Table(
    "durations_of_phase", 
    db.Column("id_flight", db.Integer, db.ForeignKey("flight.id")),
    db.Column("id_phase", db.Integer, db.ForeignKey("phases_of_flight.id"))
    )
