from flask import request, jsonify
from app.models.direction import Direction
from app.api import bp
from app.api.auth import token_auth


@bp.route('/directions', methods=['GET'])
@token_auth.login_required
def get_directions():
    page = request.args.get('page', 1, type=int)
    per_page = min(request.args.get('per_page', 10, type=int), 100)
    data = Direction.to_collection_dict(
        Direction.query,
        page,
        per_page,
        'api.get_directions'
    )
    return jsonify(data)
