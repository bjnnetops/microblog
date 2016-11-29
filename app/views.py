from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm

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

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('login.html',
                           title='Sign In',
                           form=form)