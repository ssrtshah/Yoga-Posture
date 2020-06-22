import flask as f 
import runmain as rm
import firebase


config = {
  	'apiKey': "AIzaSyBdU-_imb_PeInxnppFfzi-eoLqp7icRmY",
    'authDomain': "yogi-35620.firebaseapp.com",
    'databaseURL': "https://yogi-35620.firebaseio.com",
    'projectId': "yogi-35620",
    'storageBucket': "yogi-35620.appspot.com",
    'messagingSenderId': "476545567005",
    'appId': "1:476545567005:web:3c2ffc9d0248d53aa4f9f4",
    'measurementId': "G-VJ2RRSM282"
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