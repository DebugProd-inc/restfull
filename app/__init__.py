from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config


app = Flask(__name__)  # noqa
app.config.from_object(Config)  # noqa

db = SQLAlchemy(app)  # noqa
migrate = Migrate(app, db)  # noqa

from app import router
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

from app.api import bp as api_bp
app.register_blueprint(api_bp, url_prefix='/api')
