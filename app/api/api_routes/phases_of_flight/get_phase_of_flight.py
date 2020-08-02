from flask import jsonify

from app.all_models import PhaseOfFlight
from app.api import bp
from app.api.auth import token_auth


@bp.route('/phases_of_flight/<int:id>', methods=['GET'])
@token_auth.login_required
def get_phase_of_flight(id):
    return jsonify(PhaseOfFlight.query.get_or_404(id).to_dict())
