from flask import Flask , request , render_template , jsonify
import db

app = Flask(__name__)


@app.route('/UpdateWeight')
def changeweight():
    userID = request.args.get('userid')
    newWeight = int(request.args.get('weight'))
    db.updateWeight(userID , newWeight)
    return 'Weight updated successfully'

@app.route('/userReport')
def generateReport():
    userID = request.args.get('userid')
    return jsonify(db.userReport(userID))

@app.route('/prevUserReport')
def generatePrevReport():
    userID = request.args.get('userid')
    month = int(request.args.get('month'))
    return jsonify(db.prevUserReport(userID , month))


@app.route('/updateActivity')
def updateActivity():
    userID = request.args.get('userid') 
    minutes = int(request.args.get('minutes'))
    db.updateUserActivity(userID,minutes)
    return 'Activity Recorded'

@app.route('/createUser')
def newUser():
    userID = request.args.get('userid')
    weight = int(request.args.get('weight'))
    db.newUser(userID,weight)
    return ' '
    
@app.route('/resetProgress')
def reset():
    userID = request.args.get('userid')
    db.resetReport(userID)
    return ' '



if __name__ == "__main__":
    app.run(debug = True)
