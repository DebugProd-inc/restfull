from flask import jsonify

from app.all_models import Subsystem
from app.api import bp
from app.api.auth import token_auth


@bp.route('/subsystems/<int:id>', methods=['GET'])
@token_auth.login_required
def get_subsystem(id):
    return jsonify(Subsystem.query.get_or_404(id).to_dict())
