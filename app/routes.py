from flask import render_template
from app import app

@app.route('/')
@app.route('/index')

def index():
	user = {'username': 'Miguel'}
	return render_template('index.html', title='Home', user=user)

@app.route('/blog')
def blog_page():
	msg = {'welcome': 'Welcome to my first microblog :)'}
	return render_template('blog.html', title='Blog', msg=msg)
