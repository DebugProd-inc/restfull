from flask import request, jsonify
from app import db
from app.models.parameter import Parameter
from app.api import bp
from app.api.auth import token_auth
from app.api.errors import bad_request


@bp.route('/parameters/<int:id>', methods=['PUT'])
@token_auth.login_required
def update_parameter(id):
    parameter = Parameter.query.get_or_404(id)
    data = request.get_json() or {}
    parameter.from_dict(data)
    db.session.commit()
    return jsonify(parameter.to_dict())
