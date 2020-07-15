from flask import request, jsonify
from app.models.duration_of_phase import duration_of_phase
from app.api import bp
from app.api.auth import token_auth


@bp.route('/duration_of_phases', methods=['GET'])
@token_auth.login_required
def get_duration_of_phases():
    page = request.args.get('page', 1, type=int)
    per_page = min(request.args.get('per_page', 10, type=int), 100)
    data = duration_of_phase.to_collection_dict(
        duration_of_phase.query,
        page,
        per_page,
        'api.get_duration_of_phases'
    )
    return jsonify(data)