import os
from flask import jsonify
from app import app
from app.api import bp


@bp.route('/uploaded_files', methods=['GET'])
def uploaded_files():
    response = jsonify(
        str.join('\n', os.listdir(app.config['UPLOADED_DOCS_DEST']))
    )
    response.status_code = 200
    response.headers['Location'] = url_for(
        'api.uploaded_files'
    )
    return response
