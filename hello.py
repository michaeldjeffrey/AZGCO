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

@app.route("/")
def index():
	return render_template('index.html')

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
<<<<<<< HEAD
			'status' 					: 'Success',
=======
			'status' 					: 'Pending',
>>>>>>> hotfix/status_change
			'timeSubmitted'   : {
				'date': datetime.now().strftime('%Y-%m-%d'),
				'time': datetime.now().strftime("%H:%M:%S")
				}
			}
		db.cars.insert(post)
		return render_template('thankYou.html')
	

@app.route("/admin")
@app.route("/jobs")
def jobs():
	return render_template('jobs.html', posts = db.cars.find().sort([('status', -1),("$natural", -1)]))

@app.route("/jobs/<string:state>/<string:objid>")
def job_action(state, objid):
	if state == 'delete':
		db.cars.remove({'_id': ObjectId(objid)})
	else:
		db.cars.update({'_id': ObjectId(objid)}, {"$set": {'status':state}})
	return redirect(url_for('jobs'))
	# return "%s, %s" % (objid, state)


if __name__ == '__main__':
	app.run(debug=True)