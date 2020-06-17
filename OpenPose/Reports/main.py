from flask import Flask , request , render_template
import db

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('main.html')

@app.route('/UpdateWeight')
def changeweight():
    userID = int(request.args.get('userid')) 
    newWeight = int(request.args.get('weight'))
    db.updateWeight(userID , newWeight)
    return 'Weight updated successfully'

@app.route('/userReport')
def generateReport():
    userID = int(request.args.get('userid')) 
    print( db.userReport(userID))
    return db.userReport(userID)

@app.route('/prevUserReport')
def generatePrevReport():
    userID = int(request.args.get('userid')) 
    month = int(request.args.get('month'))
    print( db.prevUserReport(userID , month))
    return db.prevUserReport(userID , month)


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
    
@app.route('/resetProgress')
def reset():
    userID = int(request.args.get('userid')) 
    db.resetReport(userID)
    return ' '

if __name__ == "__main__":
    app.run(debug = True)

