from app import app, db
from app.models.board import Board
from app.models.direction import Direction
from app.models.flight import Flight
from app.models.manufacturer import Manufacturer
from app.models.model import Model
from app.models.parameter import Parameter
from app.models.parameter_value import ParameterValue
from app.models.phase_of_flight import PhaseOfFlight
from app.models.subsystem import Subsystem
from app.models.user import User


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
