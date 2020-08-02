from flask import (
    url_for,
    request,
    jsonify
)

from app import db
from app.all_models import Direction
from app.api import bp
from app.api.errors import bad_request
from app.api.auth import token_auth


@bp.route('/directions', methods=['POST'])
@token_auth.login_required
def create_direction():
    data = request.get_json() or {}
    if 'point_of_departure' not in data or \
            'point_of_destination' not in data:
        return bad_request(
            'must include point_of_departure, '
            + 'point_of_destination fields'
        )

    direction = Direction()
    direction.from_dict(data)
    db.session.add(direction)
    db.session.commit()
    response = jsonify(direction.to_dict())
    response.status_code = 201
    response.headers['Location'] = url_for(
        'api.get_direction',
        id=direction.id
    )
    return response
