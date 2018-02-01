from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from flask import Flask, render_template, request
from flask_heroku import Heroku
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./test.db'
heroku = Heroku(app)
db = SQLAlchemy(app)

class Soul(db.Model):
	__tablename__ = "posts"
	id = db.Column('id', db.Integer, primary_key=True)
	user_name = db.Column('user_name', db.Unicode)
	thoughts = db.Column('thoughts', db.Integer)

	def __init__(self, user_name, thoughts):
		self.user_name = user_name
		self.thoughts = thoughts

@app.route('/')
def hello_world():
	
	# user = user.query.filter_by()
	return render_template('aboutsection.html') 

@app.route('/post')
def my_favorite_quote():
	return render_template("post.html")

@app.route('/add_post' , methods=['POST'])
def another_post():
	user_name = request.form['user_name']
	thoughts = request.form['thoughts']

	reg = Soul(user_name, thoughts)
	db.session.add(reg)
	db.session.commit()
	posts = Soul.query.all()
	return render_template('profile.html', posts= posts)

@app.route('/submit_form', methods=['POST'])
def submit_form():
	user_name = request.form['user_name']
	thoughts = request.form['thoughts']

	# gives you all the users in your table
	


@app.route('/about')
def my_thoughts():
	return render_template('about.html')

@app.route('/aboutsection')
def my_thought():
	return render_template('aboutsection.html')

@app.route('/profile')
def profile():
	return render_template('profile.html')

@app.route('/books')
def my_favourite_book():
	posts = Soul.query.all()
	return render_template('working.html', posts = posts)
	return 'My favourite book is Everything Everything'

@app.route('/user/<username>')
def show_user_profile(username):
    return username

@app.route('/calculator/<num1>/<num2>/<operator>')
def show_result(num1, num2, operator):
	num1 = int(num1)
	num2 = int(num2)
	result = 0
	if operator == "+":
		result= num1 + num2 
	if operator == "-":
		result= num1- num2
	if operator == "/":
		if num2 != 0:
			result = num1 / num2 
	if operator == "*":
		result = num1 * num2 

	return str(result)

db.create_all()
# print('hi')
# app.run()
