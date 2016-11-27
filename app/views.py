from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Jesse'}
    posts = [
        {
            'author': {'nickname': 'Badger Bob'},
            'body': 'A great day for Hockey'
        },
        {
            'author': {'nickname': 'Staff'},
            'body': 'A great day for Beer'
        }
    ]
    return render_template('index.html',
                           title='Home',
                           user=user,
                           posts=posts)
