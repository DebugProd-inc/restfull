from flask import url_for, request, jsonify
from app import db
from app.models.model import Model
from app.api import bp
from app.api.errors import bad_request
from app.api.auth import token_auth


@bp.route('/models', methods=['POST'])
@token_auth.login_required
def create_model():
    data = request.get_json() or {}
    if 'name' not in data or \
            'id_manufacturer' not in data:
        return bad_request('must include name, \
            id_manufacturer fields')

    model = Model()
    model.from_dict(data)
    db.session.add(model)
    db.session.commit()
    response = jsonify(model.to_dict())
    response.status_code = 201
    response.headers['Location'] = url_for(
        'api.get_model',
        id=model.id
    )
    return response