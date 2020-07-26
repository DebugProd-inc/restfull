from flask import url_for, request, jsonify
from app import db
from app.models.subsystem import Subsystem
from app.api import bp
from app.api.errors import bad_request
from app.api.auth import token_auth


@bp.route('/subsystems', methods=['POST'])
@token_auth.login_required
def create_subsystem():
    data = request.get_json() or {}
    if 'name' not in data or \
            'id_board' not in data:
        return bad_request('must include name, \
id_board fields')

    subsystem = Subsystem()
    subsystem.from_dict(data)
    db.session.add(subsystem)
    db.session.commit()
    response = jsonify(subsystem.to_dict())
    response.status_code = 201
    response.headers['Location'] = url_for(
        'api.create_subsystem'
    )
    return response
