from flask import jsonify
from app.models.parameter_value import ParameterValue
from app.api import bp
from app.api.auth import token_auth


@bp.route('/parameter_values/<int:id>', methods=['GET'])
@token_auth.login_required
def get_parameter_value(id):
    return jsonify(ParameterValue.query.get_or_404(id).to_dict())