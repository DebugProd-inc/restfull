from flask import jsonify
from app.models.parameter import Parameter
from app.api import bp
from app.api.auth import token_auth


@bp.route('/parameters/<int:id>', methods=['GET'])
@token_auth.login_required
def get_parameter(id):
    return jsonify(Parameter.query.get_or_404(id).to_dict())
