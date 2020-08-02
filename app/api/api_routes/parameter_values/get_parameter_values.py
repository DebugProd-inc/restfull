from flask import request, jsonify

from app.all_models import ParameterValue
from app.api import bp
from app.api.auth import token_auth


@bp.route('/parameter_values', methods=['GET'])
@token_auth.login_required
def get_parameter_values():
    page = request.args.get('page', 1, type=int)
    per_page = min(request.args.get('per_page', 10, type=int), 100)
    data = ParameterValue.to_collection_dict(
        ParameterValue.query,
        page,
        per_page,
        'api.get_parameter_values'
    )
    return jsonify(data)
