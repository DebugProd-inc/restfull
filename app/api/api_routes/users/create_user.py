from flask import url_for, request, jsonify
from app import db
from app.models.user import User
from app.api import bp
from app.api.errors import bad_request
import json


@bp.route('/users', methods=['POST'])
def create_user():

    data = json.loads(request.get_data())
    if 'username' not in data or 'email' not in data or 'password' not in data:
        return bad_request('must include username, email and password fields')
    if User.query.filter_by(username=data['username']).first():
        return bad_request('please use a different username')
    if User.query.filter_by(email=data['email']).first():
        return bad_request('please use a different email address')
    user = User()
    user.from_dict(data, new_user=True)
    db.session.add(user)
    db.session.commit()
    users_dict = user.to_dict()
    users_dict["token"] = user.get_token()
    response = jsonify(users_dict)
    response.status_code = 201
    response.headers['Location'] = url_for('api.create_user', id=user.id)
    return response

    # https://debug-product-test.web.app/
