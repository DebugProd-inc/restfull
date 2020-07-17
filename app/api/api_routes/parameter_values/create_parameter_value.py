from flask import url_for, request, jsonify
from app import db
from app.models.parameter_value import ParameterValue
from app.api import bp
from app.api.errors import bad_request
from app.api.auth import token_auth


@bp.route('/parameter_values', methods=['POST'])
@token_auth.login_required
def create_parameter_value():
    data = request.get_json() or {}
    if 'id_parameter' not in data or \
            'time' not in data or \
                'value' not in data or \
                    'id_flight' not in data:
        return bad_request('must include id_parameter, \
            time, value, id_flight fields')

    parameter_value = ParameterVale()
    parameter_value.from_dict(data)
    db.session.add(parameter_value)
    db.session.commit()
    response = jsonify(parameter_value.to_dict())
    response.status_code = 201
    response.headers['Location'] = url_for(
        'api.get_parameter_value',
        id=parameter_value.id
    )
    return response