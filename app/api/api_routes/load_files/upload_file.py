from flask import request, url_for, jsonify
from flask_uploads import UploadSet, configure_uploads, DATA

from app import app
from app.api import bp

docs = UploadSet('docs', DATA)

configure_uploads(app, docs)


@bp.route('/upload', methods=['POST'])
def upload():
    if 'info' in request.files:
        file = docs.save(request.files['info'])
        response = jsonify(f'file "{file}" is loaded')
        response.status_code = 201
        response.headers['Location'] = url_for(
            'api.upload'
        )
        return response
