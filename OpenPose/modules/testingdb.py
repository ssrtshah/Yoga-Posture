import pymongo

myclient = pymongo.MongoClient("mongodb+srv://Priya:Priya@cluster0-qsi5l.mongodb.net/test")
mydb = myclient["MyDB"]
mycol = mydb["MyColl"]

for x in mycol.find():
	print (x)