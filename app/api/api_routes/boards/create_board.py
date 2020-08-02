from flask import (
    url_for,
    request,
    jsonify
)

from app import db
from app.all_models import Board
from app.api import bp
from app.api.errors import bad_request
from app.api.auth import token_auth


@bp.route('/boards', methods=['POST'])
@token_auth.login_required
def create_board():
    data = request.get_json() or {}
    if 'registration_number' not in data or \
        'id_model' not in data or \
            'year_of_manufacture' not in data:
        return bad_request(
            'must include registration_number, '
            + 'id_model, year_of_manufacture fields'
        )
    nu = Board.query.filter_by(registration_number=data['registration_number'])
    if nu.first():
        return bad_request('please use a different registration_number')

    board = Board()
    board.from_dict(data)
    db.session.add(board)
    db.session.commit()
    response = jsonify(board.to_dict())
    response.status_code = 201
    response.headers['Location'] = url_for(
        'api.get_board',
        registration_number=board.registration_number
    )
    return response
