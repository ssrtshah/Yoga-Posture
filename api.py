import flask as f 
import runmain as rm
import firebase
import Reports.db as db


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

@app.route('/UpdateWeight')
def changeweight():
    userID = f.request.args.get('userid')
    newWeight = int(f.request.args.get('weight'))
    db.updateWeight(userID , newWeight)
    return 'Weight updated successfully'

@app.route('/userReport')
def generateReport():
    userID = f.request.args.get('userid')
    return f.jsonify(db.userReport(userID))

@app.route('/prevUserReport')
def generatePrevReport():
    userID = f.request.args.get('userid')
    month = int(f.request.args.get('month'))
    return f.jsonify(db.prevUserReport(userID , month))


@app.route('/updateActivity')
def updateActivity():
    userID = f.request.args.get('userid') 
    minutes = int(f.request.args.get('minutes'))
    db.updateUserActivity(userID,minutes)
    return 'Activity Recorded'

@app.route('/createUser')
def newUser():
    userID = f.request.args.get('userid')
    weight = int(f.request.args.get('weight'))
    db.newUser(userID,weight)
    return ' '
    
@app.route('/resetProgress')
def reset():
    userID = f.request.args.get('userid')
    db.resetReport(userID)
    return ' '


if __name__ == '__main__':
	app.run()