
from datetime import datetime
from flask import render_template
from Website import app

@app.route('/')
@app.route('/home')
def home():
    return render_template(
        'home.html',
        title = 'home',
        year=datetime.now().year
    )

@app.route('/education')
def education():
    return render_template(
        'education.html',
        title = 'education',
        year=datetime.now().year
    )

@app.route('/experience')
def experience():
    return render_template(
        'experience.html',
        title = 'experience',
        year=datetime.now().year
    )

@app.route('/projects')
def projects():
    return render_template(
        'projects.html',
        title = 'projects',
        year=datetime.now().year
    )

@app.route('/links')
def links():
    return render_template(
        'links.html',
        title = 'interesting links',
        year=datetime.now().year
    )