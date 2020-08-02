from flask import request, jsonify

from app.all_models import PhaseOfFlight
from app.api import bp
from app.api.auth import token_auth


@bp.route('/phases_of_flight', methods=['GET'])
@token_auth.login_required
def get_phases_of_flight():
    page = request.args.get('page', 1, type=int)
    per_page = min(request.args.get('per_page', 10, type=int), 100)
    data = PhaseOfFlight.to_collection_dict(
        PhaseOfFlight.query,
        page,
        per_page,
        'api.get_phases_of_flight'
    )
    return jsonify(data)
