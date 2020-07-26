from flask import url_for, request, jsonify
from app import db
from app.models.phase_of_flight import PhaseOfFlight
from app.api import bp
from app.api.errors import bad_request
from app.api.auth import token_auth


@bp.route('/phases_of_flight', methods=['POST'])
@token_auth.login_required
def create_phase_of_flight():
    data = request.get_json() or {}
    if 'name' not in data:
        return bad_request('must include name field')

    phase_of_flight = PhaseOfFlight()
    phase_of_flight.from_dict(data)
    db.session.add(phase_of_flight)
    db.session.commit()
    response = jsonify(phase_of_flight.to_dict())
    response.status_code = 201
    response.headers['Location'] = url_for(
        'api.get_phase_of_flight',
        id=phase_of_flight.id
    )
    return response