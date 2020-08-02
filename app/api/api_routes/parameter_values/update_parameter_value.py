from flask import request, jsonify

from app import db
from app.all_models import ParameterValue
from app.api import bp
from app.api.auth import token_auth
from app.api.errors import bad_request


@bp.route('/parameter_values/<int:id>', methods=['PUT'])
@token_auth.login_required
def update_parameter_value(id):
    parameter_value = ParameterValue.query.get_or_404(id)
    data = request.get_json() or {}
    parameter_value.from_dict(data)
    db.session.commit()
    return jsonify(parameter_value.to_dict())
