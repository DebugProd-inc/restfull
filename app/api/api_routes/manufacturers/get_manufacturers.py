from flask import request, jsonify
from app.models.manufacturer import Manufacturer
from app.api import bp
from app.api.auth import token_auth


@bp.route('/manufacturers', methods=['GET'])
@token_auth.login_required
def get_manufacturers():
    page = request.args.get('page', 1, type=int)
    per_page = min(request.args.get('per_page', 10, type=int), 100)
    data = Manufacturer.to_collection_dict(
        Manufacturer.query,
        page,
        per_page,
        'api.get_manufacturers'
    )
    return jsonify(data)