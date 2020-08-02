from app import app, db
from app.all_models import *


@app.shell_context_processor
def make_shell_context():
    return {
        'db': db,
        'Board': Board,
        'Direction': Direction,
        'Flight': Flight,
        'Manufacturer': Manufacturer,
        'Model': Model,
        'Parameter': Parameter,
        'ParameterValue': ParameterValue,
        'PhaseOfFlight': PhaseOfFlight,
        'Subsystem': Subsystem,
        'User': User
    }
