from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
	return '<h1> <i> I live in Palestine </i> </h1>'

@app.route('/quotes')
def my_favorite_quote():
	return 'You left my mind pregnant with babies called memories'

@app.route('/books')
def my_favourite_book():
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
