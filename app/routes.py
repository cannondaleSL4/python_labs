from app import app

@app.route('/')
@app.route('/index')
def index_page():
    return 'Hello World!'