from app.api import bp


@bp.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
    pass
