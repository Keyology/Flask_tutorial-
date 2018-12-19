from flask import render_template
from app import app 
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def idex():
    user = {'username': "Keoni Murray"}
    posts = [{'author': {'username':'Keoni Murray'}, 'body': "The emo Life"}, 
    {'author': {'username': 'tysuomi'}, 
    'body': 'feel the power of my sharingan'},]
    return render_template('index.html', title="home", user=user, posts=posts)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title="signin", form=form)