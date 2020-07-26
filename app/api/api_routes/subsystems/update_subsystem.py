from flask import request, jsonify
from app import db
from app.models.subsystem import Subsystem
from app.api import bp
from app.api.auth import token_auth
from app.api.errors import bad_request


@bp.route('/subsystems/<int:id>', methods=['PUT'])
@token_auth.login_required
def update_subsystem(id):
    subsystem = Subsystem.query.get_or_404(id)
    data = request.get_json() or {}
    subsystem.from_dict(data)
    db.session.commit()
    return jsonify(subsystem.to_dict())
