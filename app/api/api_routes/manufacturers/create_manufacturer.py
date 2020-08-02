from flask import (
    url_for,
    request,
    jsonify
)

from app import db
from app.all_models import Manufacturer
from app.api import bp
from app.api.errors import bad_request
from app.api.auth import token_auth


@bp.route('/manufacturers', methods=['POST'])
@token_auth.login_required
def create_manufacturer():
    data = request.get_json() or {}
    if 'name' not in data:
        return bad_request('must include name field')

    manufacturer = Manufacturer()
    manufacturer.from_dict(data)
    db.session.add(manufacturer)
    db.session.commit()
    response = jsonify(manufacturer.to_dict())
    response.status_code = 201
    response.headers['Location'] = url_for(
        'api.get_manufacturer',
        id=manufacturer.id
    )
    return response
