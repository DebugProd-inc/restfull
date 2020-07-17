from flask import request, jsonify
from app import db
from app.models.flight import Flight
from app.api import bp
from app.api.auth import token_auth
from app.api.errors import bad_request


@bp.route('/flights/<int:id>', methods=['PUT'])
@token_auth.login_required
def update_flight(id):
    flight = Flight.query.get_or_404(id)
    data = request.get_json() or {}
    flight.from_dict(data)
    db.session.commit()
    return jsonify(flight.to_dict())
