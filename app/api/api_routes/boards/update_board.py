from flask import request, jsonify
from app import db
from app.models.board import Board
from app.api import bp
from app.api.auth import token_auth
from app.api.errors import bad_request


@bp.route('/boards/<registration_number>', methods=['PUT'])
@token_auth.login_required
def update_board(registration_number):
    board = Board.query.get_or_404(registration_number)
    data = request.get_json() or {}
    if 'registration_number' not in data:
        return bad_request('no such registration number in DB')
    bq = Board.query.filter_by(registration_number=data['registration_number'])
    if data['registration_number'] != board.registration_number and \
            bq.first():
        return bad_request('please use a different registration_number')
    board.from_dict(data)
    db.session.commit()
    return jsonify(board.to_dict())
