from flask import jsonify

from app.all_models import Flight
from app.api import bp
from app.api.auth import token_auth


@bp.route('/flights/<int:id>', methods=['GET'])
@token_auth.login_required
def get_flight(id):
    return jsonify(Flight.query.get_or_404(id).to_dict())
