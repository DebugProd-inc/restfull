from flask import request, jsonify
from app.models.board import Board
from app.api import bp
from app.api.auth import token_auth


@bp.route('/boards', methods=['GET'])
@token_auth.login_required
def get_boards():
    page = request.args.get('page', 1, type=int)
    per_page = min(request.args.get('per_page', 10, type=int), 100)
    data = Board.to_collection_dict(
        Board.query,
        page,
        per_page,
        'api.get_boards'
    )
    return jsonify(data)
