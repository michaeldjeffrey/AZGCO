from flask import (Flask,
	render_template, request)
#TODO - import pymongo
#TODO - name pymongo database (cars?)
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
	return "You drive a %s %s?" % (make, model)

@app.route("/result/")
def showdb():
	#TODO - show results in pymongo DB



if __name__ == '__main__':
	app.run(debug=True)