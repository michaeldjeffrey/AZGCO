from flask import (
	Flask,
	render_template, 
	request,
	make_response,
	flash)

from pymongo import Connection
db = Connection().test


app = Flask(__name__)
app.secret_key = 'some_secret'


@app.route("/")
def index():
	count = 0
	resp = make_response(render_template('index.html', carsAmount = 10))
	if 'number_of_cars' in request.cookies:
		count = db.cars.count()
		resp.set_cookie('number_of_cars', count)
	else:
		count = request.cookies.get('number_of_cars')
	return resp


@app.route("/hello/")
@app.route("/hello/<name>")
def hello(name=None):
	return render_template('hello.html', name=name)

@app.route("/result/", methods=['POST', 'GET'])
@app.route("/result", methods=['POST', 'GET'])
def result():
	if request.method == 'POST':
		make = request.form['make']
		model = request.form['model']
		resp = make_response(render_template('showCars.html', make=make, model=model, cars=db.cars.find()))
		resp.set_cookie('make', make)
		resp.set_cookie('model', model)
		db.cars.insert({'make': make, 'model': model})
		return resp
	else:
		return showdb()

def showdb():
	make = request.cookies.get('make')
	model = request.cookies.get('model')
	return render_template('showCars.html',make=make, model=model, cars = db.cars.find())

@app.route('/users')
def name():
	return render_template('users.html', users=db.people.find())
			


if __name__ == '__main__':
	app.run(debug=True)