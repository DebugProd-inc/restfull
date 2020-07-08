from app.api import bp


@bp.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    pass
