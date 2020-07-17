from flask import request
from flask_uploads import UploadSet, configure_uploads, DATA

from app import app
from app.api import bp

docs = UploadSet('docs', DATA)

configure_uploads(app, docs)


@bp.route('/upload', methods=['POST'])
def upload():
    if 'file' in request.files:
        filename = docs.save(request.files['file'])
        return filename
