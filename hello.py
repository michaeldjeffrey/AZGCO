from flask import (Flask,
	render_template, request)

from pymongo import Connection
db = Connection().test


app = Flask(__name__)


@app.route("/")
def index():
	return "Hello Michael Jeffrey"

@app.route("/hello/")
@app.route("/hello/<name>")
def hello(name=None):
	return render_template('hello.html', name=name)

@app.route("/result", methods=['POST', 'GET'])
def result():
	#TODO - Insert make and model into pymongo db
	make = request.form['make']
	model = request.form['model']
	db.cars.insert({'make': make, 'model': model})
	return "You drive a %s %s? Well I hope so becaues now its in the database" % (make, model)

@app.route("/result/")
def showdb():
	return render_template('showCars.html', cars = db.cars.find())


if __name__ == '__main__':
	app.run(debug=True)