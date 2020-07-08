from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config
from app.api import bp as api_bp


app = Flask(__name__)  # noqa
app.config.from_object(Config)  # noqa
app.register_blueprint(api_bp, url_prefix='/api')  # noqa
db = SQLAlchemy(app)  # noqa
migrate = Migrate(app, db)  # noqa

from app import router, models
