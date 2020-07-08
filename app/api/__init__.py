from flask import Blueprint

bp = Blueprint('api', __name__)  # noqa

from app.api import errors, tokens, api_router
