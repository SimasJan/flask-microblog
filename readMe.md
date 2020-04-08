### Chapter 3 - Forms

### Installing flask-WTF extension


### Configuration

But for any applications except the simplest ones, you are going to find that Flask (and possibly also the Flask extensions that you use) offer some amount of freedom in how to do things, and you need to make some decisions, which you pass to the framework as a list of configuration variables.

There are several formats for the application to specify configuration options. The most basic solution is to define your variables as keys in app.config, which uses a dictionary style to work with variables. 

While the above syntax is sufficient to create configuration options for Flask, I like to enforce the principle of separation of concerns, so instead of putting my configuration in the same place where I create my application I will use a slightly more elaborate structure that allows me to keep my configuration in a separate file.

A format that I really like because it is very extensible, is to use a class to store configuration variables. To keep things nicely organized, I'm going to create the configuration class in a separate Python module. Below you can see the new configuration class for this application, stored in a config.py module in the top-level directory.

The SECRET_KEY configuration variable that I added as the only configuration item is an important part in most Flask applications. Flask and some of its extensions use the value of the secret key as a cryptographic key, useful to generate signatures or tokens. The Flask-WTF extension uses it to protect web forms against a nasty attack called Cross-Site Request Forgery or CSRF (pronounced "seasurf"). As its name implies, the secret key is supposed to be secret, as the strength of the tokens and signatures generated with it depends on no person outside of the trusted maintainers of the application knowing it.

The value of the secret key is set as an expression with two terms, joined by the or operator. The first term looks for the value of an environment variable, also called SECRET_KEY. The second term, is just a hardcoded string. This is a pattern that you will see me repeat often for configuration variables. The idea is that a value sourced from an environment variable is preferred, but if the environment does not define the variable, then the hardcoded string is used instead. When you are developing this application, the security requirements are low, so you can just ignore this setting and let the hardcoded string be used. But when this application is deployed on a production server, I will be setting a unique and difficult to guess value in the environment, so that the server has a secure key that nobody else knows.

Now that I have a config file, I need to tell Flask to read it and apply it. That can be done right after the Flask application instance is created using the app.config.from_object() method, within the app/__init__.py file.

### User Login Form

- Backend
The Flask-WTF extension uses Python classes to represent web forms. A form class simply defines the fields of the form as class variables.

Once again having separation of concerns in mind, I'm going to use a new app/forms.py module to store my web form classes. To begin, let's define a user login form, which asks the user to enter a username and a password. The form will also include a "remember me" check box, and a submit button.

- Front End

The next step is to add the form to an HTML template so that it can be rendered on a web page. The good news is that the fields that are defined in the LoginForm class know how to render themselves as HTML, so this task is fairly simple. Below you can see the login template, which I'm going to store in file app/templates/login.html
