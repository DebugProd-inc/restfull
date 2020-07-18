import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    # secret key
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'kaf704-is-impregnable'

    # working with DB
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # working with tokens
    TOKEN_LIFE_TIME = 900

    # working with files
    UPLOADED_DOCS_DEST = os.path.abspath("static\\docs")
