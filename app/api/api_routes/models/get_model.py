from flask import jsonify
from app.models.model import Model
from app.api import bp
from app.api.auth import token_auth


@bp.route('/models/<int:id>', methods=['GET'])
@token_auth.login_required
def get_model(id):
    return jsonify(Model.query.get_or_404(id).to_dict())
