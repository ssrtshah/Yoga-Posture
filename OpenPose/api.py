import flask as f 
import runmain as rm

app = f.Flask(__name__)

@app.route('/getvalue',methods=['GET'])
def getvalue():
	asana = str(f.request.args['asana'])
	rm.getvaluesfromdb(asana)
	return 'got asana'

@app.route('/compareImage',methods=['GET'])
def compareImage():
	d={}
	imagefile = str(f.request.args['imagefile'])
	avg=rm.takeAndCompare(imagefile)
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