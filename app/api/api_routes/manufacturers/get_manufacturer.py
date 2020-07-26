from flask import jsonify
from app.models.manufacturer import Manufacturer
from app.api import bp
from app.api.auth import token_auth


@bp.route('/manufacturers/<int:id>', methods=['GET'])
@token_auth.login_required
def get_manufacturer(id):
    return jsonify(Manufacturer.query.get_or_404(id).to_dict())
