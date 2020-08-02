from flask import request, jsonify

from app import db
from app.all_models import Manufacturer
from app.api import bp
from app.api.auth import token_auth
from app.api.errors import bad_request


@bp.route('/manufacturers/<int:id>', methods=['PUT'])
@token_auth.login_required
def update_manufacturer(id):
    manufacturer = Manufacturer.query.get_or_404(id)
    data = request.get_json() or {}
    manufacturer.from_dict(data)
    db.session.commit()
    return jsonify(manufacturer.to_dict())
