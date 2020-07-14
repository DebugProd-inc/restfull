from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config


app = Flask(__name__)  # noqa
app.config.from_object(Config)  # noqa

db = SQLAlchemy(app)  # noqa
migrate = Migrate(app, db)  # noqa

from app import router
from app.all_models import *

from app.api import bp as api_bp
app.register_blueprint(api_bp, url_prefix='/api')
