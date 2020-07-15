from flask import url_for, request, jsonify
from app import db
from app.models.user import User
from app.api import bp
from app.api.errors import bad_request
import json


@bp.route('/user', methods=['POST'])
def create_user():
    data = json.loads(request.get_data()) or {}
    print(111111111111111111111, 'email' in data,
          'username' in data, 'password' in data)
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
    response = jsonify(user.to_dict())
    response.status_code = 201
    response.headers['Location'] = url_for('api.get_user', id=user.id)
    return response
