from app import app, db, modeller


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User}
