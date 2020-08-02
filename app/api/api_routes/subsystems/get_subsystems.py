from flask import request, jsonify

from app.all_models import Subsystem
from app.api import bp
from app.api.auth import token_auth


@bp.route('/subsystems', methods=['GET'])
@token_auth.login_required
def get_subsystems():
    page = request.args.get('page', 1, type=int)
    per_page = min(request.args.get('per_page', 10, type=int), 100)
    data = Subsystem.to_collection_dict(
        Subsystem.query,
        page,
        per_page,
        'api.get_subsystems'
    )
    return jsonify(data)
