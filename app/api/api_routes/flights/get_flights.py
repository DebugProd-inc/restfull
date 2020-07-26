from flask import request, jsonify
from app.models.flight import Flight
from app.api import bp
from app.api.auth import token_auth


@bp.route('/flights', methods=['GET'])
@token_auth.login_required
def get_flights():
    page = request.args.get('page', 1, type=int)
    per_page = min(request.args.get('per_page', 10, type=int), 100)
    data = Flight.to_collection_dict(
        Flight.query,
        page,
        per_page,
        'api.get_flights'
    )
    return jsonify(data)