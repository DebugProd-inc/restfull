from flask import request, jsonify
from app import db
from app.models.phase_of_flight import PhaseOfFlight
from app.api import bp
from app.api.auth import token_auth
from app.api.errors import bad_request


@bp.route('/phases_of_flight/<int:id>', methods=['PUT'])
@token_auth.login_required
def update_phase_of_flight(id):
    phase_of_flight = PhaseOfFlight.query.get_or_404(id)
    data = request.get_json() or {}
    phase_of_flight.from_dict(data)
    db.session.commit()
    return jsonify(phase_of_flight.to_dict())
