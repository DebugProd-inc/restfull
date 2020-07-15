from flask import url_for, request, jsonify
from app import db
from app.models.duration_of_phase import duration_of_phase
from app.api import bp
from app.api.errors import bad_request
from app.api.auth import token_auth


@bp.route('/duration_of_phases', methods=['POST'])
@token_auth.login_required
def create_duration_of_phase():
    data = request.get_json() or {}
    if 'id_flight' not in data or \
            'id_phase' not in data or \
                'start_phase' not in data or \
                    'end_phase' not in data:
        return bad_request('must include id_flight, \
            id_phase, start_phase, end_phase fields')

    duration_of_phase = duration_of_phase()
    duration_of_phase.from_dict(data)
    db.session.add(duration_of_phase)
    db.session.commit()
    response = jsonify(duration_of_phase.to_dict())
    response.status_code = 201
    response.headers['Location'] = url_for(
        'api.get_duration_of_phase',
        id=duration_of_phase.id
    )
    return response