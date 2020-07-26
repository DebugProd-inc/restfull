from flask import request, jsonify
from app import db
from app.models.model import Model
from app.api import bp
from app.api.auth import token_auth
from app.api.errors import bad_request


@bp.route('/models/<int:id>', methods=['PUT'])
@token_auth.login_required
def update_model(id):
    model = Model.query.get_or_404(id)
    data = request.get_json() or {}
    model.from_dict(data)
    db.session.commit()
    return jsonify(model.to_dict())
