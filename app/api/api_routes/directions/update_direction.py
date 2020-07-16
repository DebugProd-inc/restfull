from flask import request, jsonify
from app import db
from app.models.direction import Direction
from app.api import bp
from app.api.auth import token_auth
from app.api.errors import bad_request


@bp.route('/directions/<int:id>', methods=['PUT'])
@token_auth.login_required
def update_direction(id):
    direction = Direction.query.get_or_404(id)
    data = request.get_json() or {}
    direction.from_dict(data)
    db.session.commit()
    return jsonify(direction.to_dict())
