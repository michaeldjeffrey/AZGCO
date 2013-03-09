from flask import (
	Flask,
	render_template, 
	request,
	make_response,
	flash,redirect, url_for)
from datetime import (datetime, date, time)

from pymongo import Connection
from bson.objectid import ObjectId
db = Connection().test


app = Flask(__name__)
app.secret_key = 'some_secret'

carsAmount = db.cars.count()

@app.route("/test")
def test():
	post = {
		'name': '',
		'town': '',
		'status': '',
		'make': '',
		'model': '',
		'year': '',
		'serviceType': '',
		'location': '',
		'': '',
		'': '',
		'': '',
		'': '',
	}

	return render_template('jobs.html', posts = post)

@app.route("/")
def index():
	return render_template('index.html', carsAmount=carsAmount)

@app.route('/scheduleAppointment/', methods=['POST', 'GET'])
@app.route('/scheduleAppointment', methods=['POST', 'GET'])
def makeNewAppointment():
	if request.method == 'POST':
		post = {
			'make'            : request.form['make'],
			'model'           : request.form['model'],
			'year'            : request.form['year'],
			'quote'           : request.form['quote'],
			'name'            : request.form['name'],
			'email'           : request.form['email'],
			'phone'           : request.form['phone'],
			'serviceType'     : request.form['serviceType'],
			'location'        : request.form['location'],
			'contactMethod'   : request.form['contactMethod'],
			'appointmentTime' : request.form['appointmentTime'],
			'timeSubmitted'   : {
				'date': datetime.now().strftime('%Y-%m-%d'),
				'time': datetime.now().strftime("%H:%M:%S")
				}
			}
		db.cars.insert(post)
		return render_template('thankYou.html')

@app.route("/result/", methods=['POST', 'GET'])
@app.route("/result", methods=['POST', 'GET'])
def result():
	if request.method == 'POST':
		carsAmount += 1
		make = request.form['make']
		model = request.form['model']
		resp = make_response(render_template('showCars.html', carsAmount=carsAmount, make=make, model=model, cars=db.cars.find()))
		resp.set_cookie('make', make)
		resp.set_cookie('model', model)
		post = {
			'make': make,
			'model': model,
			'datetime': {
				'date': datetime.now().strftime('%Y-%m-%d'),
				'time': datetime.now().strftime("%H:%M:%S")
				}
		}
		db.cars.insert(post)
		return resp
	else:
		return showdb()

def showdb():
	make = request.cookies.get('make')
	model = request.cookies.get('model')
	return render_template('showCars.html',carsAmount=carsAmount, make=make, model=model, cars = db.cars.find())

@app.route('/users')
def name():
	return render_template('users.html', carsAmount=carsAmount, users=db.people.find())		

@app.route('/admin/')	
@app.route('/admin')
def admin():
	return render_template('admin.html')	

@app.route("/jobs")
def jobs():
	return render_template('jobs.html', posts = db.cars.find())

@app.route("/jobs/<string:state>/<string:objid>")
def job_action(state, objid):
	db.cars.update({'_id': ObjectId(objid)}, {"$set": {'status':state}})
	return redirect(url_for('jobs'))
	# return "%s, %s" % (objid, state)


if __name__ == '__main__':
	app.run(debug=True)