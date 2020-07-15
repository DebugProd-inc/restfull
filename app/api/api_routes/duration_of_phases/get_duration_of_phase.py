from flask import jsonify
from app.models.duration_of_phase import duration_of_phase
from app.api import bp
from app.api.auth import token_auth


@bp.route('/duration_of_phases/<int:id>', methods=['GET'])
@token_auth.login_required
def get_duration_of_phase(id):
    return jsonify(duration_of_phase.query.get_or_404(id).to_dict())
