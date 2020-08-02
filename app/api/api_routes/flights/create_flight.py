from flask import (
    url_for,
    request,
    jsonify
)

from app import db
from app.all_models import Flight
from app.api import bp
from app.api.errors import bad_request
from app.api.auth import token_auth


@bp.route('/flights', methods=['POST'])
@token_auth.login_required
def create_flight():
    data = request.get_json() or {}
    if 'id_board' not in data or \
            'id_direction' not in data or \
            'time_begin' not in data or \
            'date_begin' not in data:
        return bad_request(
            'must include id_board, '
            + id_direction, time_begin, date_begin fields'
        )

    flight = Flight()
    flight.from_dict(data)
    db.session.add(flight)
    db.session.commit()
    response = jsonify(flight.to_dict())
    response.status_code = 201
    response.headers['Location'] = url_for(
        'api.get_flight',
        id=flight.id
    )
    return response
