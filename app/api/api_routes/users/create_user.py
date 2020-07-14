from flask import url_for, request, jsonify
from app import db
from app.models.user import User
from app.api import bp
from app.api.errors import bad_request


@bp.route('/users', methods=['POST'])
def create_user():
    data = request.get_json() or {}
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
    # response.headers['Access-Control-Allow-Origin'] = '*'
    # response.headers["Access-Control-Allow-Methods"] = "GET, PUT, POST, DELETE"
    # response.headers["Access-Control-Allow-Headers"] = \
    # "Origin, X-Requested-With, Content-Type, Accept, Authorization"
    return response


@bp.before_request
def before_request(response):
    white_origin = ['http://localhost:8080',
                    'https://debug-product-test.web.app']
    if request.headers['Origin'] in white_origin:
        response.headers['Access-Control-Allow-Origin'] = request.headers['Origin']
        response.headers['Access-Control-Allow-Methods'] = 'PUT,GET,POST,DELETE'
        response.headers['Access-Control-Allow-Headers'] = 'Content-Type,Authorization'
    return response


@bp.after_request
def after_request(response):
    white_origin = ['http://localhost:8080',
                    'https://debug-product-test.web.app']
    if request.headers['Origin'] in white_origin:
        response.headers['Access-Control-Allow-Origin'] = request.headers['Origin']
        response.headers['Access-Control-Allow-Methods'] = 'PUT,GET,POST,DELETE'
        response.headers['Access-Control-Allow-Headers'] = 'Content-Type,Authorization'
    return response
