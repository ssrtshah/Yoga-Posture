import flask as f 
import runmain as rm
import firebase


config = {
  	'apiKey': "AIzaSyCMspprnQ4tOwDHL-DBhqhdkX8xM8SwOqU",
    'authDomain': "yoga-posture-e5cdb.firebaseapp.com",
    'databaseURL': "https://yoga-posture-e5cdb.firebaseio.com",
    'projectId': "yoga-posture-e5cdb",
    'storageBucket': "yoga-posture-e5cdb.appspot.com",
    'messagingSenderId': "649842810638",
    'appId': "1:649842810638:web:7c45a9b58c8a92dfb9815f",
    'measurementId': "G-N6574YK0PW"
}

fb = firebase.Firebase(config)

storage = fb.storage()

app = f.Flask(__name__)

@app.route('/getValue',methods=['GET'])
def getvalue():
	asana = str(f.request.args['asana'])
	rm.getvaluesfromdb(asana)
	return 'got asana'

@app.route('/compareImage',methods=['GET'])
def compareImage():
	d={}
	imagefile = str(f.request.args['imagefile'])
	storage.child(imagefile).download("new_image.jpg")
	avg=rm.takeAndCompare()
	d['avgerr']=avg
	return f.jsonify(d)

@app.route('/geterror')
def geterror():
	d={}
	errormsg=rm.findingerror()
	d['msg']=errormsg
	return f.jsonify(d)


if __name__ == '__main__':
	app.run()