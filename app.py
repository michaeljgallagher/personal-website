from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail

app = Flask(__name__)

# DEVELOPMENT
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///project_library.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = ''

# PRODUCTION
# app.config.from_pyfile('config.py')

db = SQLAlchemy(app)
mail = Mail(app)


@app.route("/", methods=['GET'])
@app.route("/home/", methods=['GET'])
def home():
	return render_template('home.html', title='Michael Gallagher', nav='home')


@app.errorhandler(404)
def not_found(e):
	return render_template('404.html', title="Not Found"), 404


import routes
