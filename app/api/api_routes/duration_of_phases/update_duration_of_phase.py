from flask import request, jsonify
from app import db
from app.models.duration_of_phase import duration_of_phase
from app.api import bp
from app.api.auth import token_auth
from app.api.errors import bad_request


@bp.route('/duration_of_phases/<int:id>', methods=['PUT'])
@token_auth.login_required
def update_duration_of_phase(id):
    duration_of_phase = duration_of_phase.query.get_or_404(id)
    data = request.get_json() or {}
    duration_of_phase.from_dict(data)
    db.session.commit()
    return jsonify(duration_of_phase.to_dict())
