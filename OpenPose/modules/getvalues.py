import pymongo

def getvalues(asana):
	myclient = pymongo.MongoClient("mongodb+srv://Priya:Priya@cluster0-qsi5l.mongodb.net/test")
	mydb = myclient["MyDB"]
	mycol = mydb["MyColl"]

	myquery={"name":asana}
	x = mycol.find_one(myquery)

	temp=[]
	lst=[]

	for i in x:
		temp.append(x[i])
	lst=temp[2:]

	return lst