from flask import jsonify
from app.models.board import Board
from app.api import bp
from app.api.auth import token_auth


@bp.route('/boards/<registration_number>', methods=['GET'])
@token_auth.login_required
def get_board(registration_number):
    return jsonify(Board.query.get_or_404(registration_number).to_dict())
