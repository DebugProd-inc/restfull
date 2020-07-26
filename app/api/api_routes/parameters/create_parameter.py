from flask import url_for, request, jsonify
from app import db
from app.models.parameter import Parameter
from app.api import bp
from app.api.errors import bad_request
from app.api.auth import token_auth


@bp.route('/parameters', methods=['POST'])
@token_auth.login_required
def create_parameter():
    data = request.get_json() or {}
    if 'name' not in data or \
            'id_subsystem' not in data:
        return bad_request('must include name, \
            id_subsystem fields')

    parameter = Parameter()
    parameter.from_dict(data)
    db.session.add(parameter)
    db.session.commit()
    response = jsonify(parameter.to_dict())
    response.status_code = 201
    response.headers['Location'] = url_for(
        'api.get_parameter',
        id=parameter.id
    )
    return response
