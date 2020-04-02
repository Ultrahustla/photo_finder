from photo_app import app

@app.route('/')
@app.route('/hello')
def hello():
    return 'Hello photographer!'