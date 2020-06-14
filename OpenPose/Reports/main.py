from flask import Flask , request , render_template
import db

app = Flask(__name__)


@app.route('/UpdateWeight')
def changeweight():
    userID = int(request.args.get('userid')) 
    newWeight = int(request.args.get('weight'))
    db.updateWeight(userID , newWeight)
    return 'Weight updated successfully'

@app.route('/userReport')
def generateReport():
    userID = int(request.args.get('userid')) 
    return db.userReport(userID)

@app.route('/updateActivity')
def updateActivity():
    userID = int(request.args.get('userid')) 
    minutes = int(request.args.get('minutes'))
    db.updateUserActivity(userID,minutes)
    return 'Activity Recorded'

@app.route('/createUser')
def newUser():
    userID = int(request.args.get('userid')) 
    weight = int(request.args.get('weight'))
    db.newUser(userID,weight)
    return ' ' 

if __name__ == "__main__":
    app.run(debug = True)

