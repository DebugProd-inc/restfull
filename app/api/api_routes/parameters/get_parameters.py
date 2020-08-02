from flask import request, jsonify

from app.all_models import Parameter
from app.api import bp
from app.api.auth import token_auth


@bp.route('/parameters', methods=['GET'])
@token_auth.login_required
def get_parameters():
    page = request.args.get('page', 1, type=int)
    per_page = min(request.args.get('per_page', 10, type=int), 100)
    data = Parameter.to_collection_dict(
        Parameter.query,
        page,
        per_page,
        'api.get_parameters'
    )
    return jsonify(data)
