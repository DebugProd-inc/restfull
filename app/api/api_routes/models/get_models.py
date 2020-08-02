from flask import request, jsonify

from app.all_models import Model
from app.api import bp
from app.api.auth import token_auth


@bp.route('/models', methods=['GET'])
@token_auth.login_required
def get_models():
    page = request.args.get('page', 1, type=int)
    per_page = min(request.args.get('per_page', 10, type=int), 100)
    data = Model.to_collection_dict(
        Model.query,
        page,
        per_page,
        'api.get_models'
    )
    return jsonify(data)
