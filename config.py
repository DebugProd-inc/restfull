import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    # secret key
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'kaf704-is-impregnable'

    # working with DB
    # postgres
    POSTGRES_URL = os.environ.get('POSTGRES_URL')
    POSTGRES_USER = os.environ.get('POSTGRES_USER')
    POSTGRES_PW = os.environ.get('POSTGRES_PW')
    POSTGRES_DB = os.environ.get('POSTGRES_DB')

    if POSTGRES_URL and POSTGRES_USER and POSTGRES_PW and POSTGRES_DB:
        PG_DB_URL = f'postgresql+psycopg2://{POSTGRES_USER}:{POSTGRES_PW}\
@{POSTGRES_URL}/{POSTGRES_DB}'
    else:
        PG_DB_URL = None

    # sqlite
    SQLITE_DB_URL = 'sqlite:///' + os.path.join(basedir, 'app.db')

    # SQLAlchemy
    SQLALCHEMY_DATABASE_URI = PG_DB_URL or SQLITE_DB_URL
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # working with tokens
    TOKEN_LIFE_TIME = 900

    # working with files
    UPLOADED_DOCS_DEST = os.path.abspath("static\\docs")
