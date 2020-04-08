from flask import render_template
from app import app

@app.route('/')
@app.route('/index')

def index():
	user = {'username': 'Miguel'}

	# creating fake posts for vistors to see
	posts = [
		{
			'author' : {'username': 'John'},
			'body' : 'Beautiful day in Portland!'
		},
		{
			'author' : {'username': 'Susan'},
			'body' : 'The Avengers movie was so cool!'
		},
		{
			'author' : {'username': 'Lily'},
			'body' : 'Coronavirus is still having a tremendious impact on the global economy.'
		},

	]
	return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/blog')
def blog_page():
	msg = {'welcome': 'Welcome to my first microblog :)'}
	return render_template('blog.html', title='Blog', msg=msg)
