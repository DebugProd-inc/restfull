from flask import jsonify
from app.models.phase_of_flight import PhaseOfFlight
from app.api import bp
from app.api.auth import token_auth


@bp.route('/phases_of_flight/<int:id>', methods=['GET'])
@token_auth.login_required
def get_phase_of_flight(id):
    return jsonify(PhaseOfFlight.query.get_or_404(id).to_dict())