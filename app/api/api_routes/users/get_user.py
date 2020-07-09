from flask import jsonify
from app.models.user import User
from app.api import bp


@bp.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    return jsonify(User.query.get_or_404(id).to_dict())
