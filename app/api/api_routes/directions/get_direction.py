from flask import jsonify
from app.models.direction import Direction
from app.api import bp
from app.api.auth import token_auth


@bp.route('/directions/<int:id>', methods=['GET'])
@token_auth.login_required
def get_direction(id):
    return jsonify(Direction.query.get_or_404(id).to_dict())
