import pymongo
from datetime import date 

myclient = pymongo.MongoClient("mongodb+srv://Priya:Priya@cluster0-qsi5l.mongodb.net/test")
mydb = myclient["MyDB"]
mycol = mydb["Sample"]

def updateWeight(userid , new_weight):
    myuser = { "user_id" :userid}
    newquery = { "$set": { "cur_weight": new_weight} }
    mycol.update_one(myuser,newquery)

def userReport(userid):
    for data in mycol.find( {"user_id":userid} , {"date":1 , "minutes":1 , "cal_burnt":1 , "total_min":1 ,  "total_cal":1 , "minutes_whole":1 , "calories_whole":1 , "_id":0} ):
            pass
    return data

def newUser(userid , weight):
    day=date.today().day
    month=date.today().month
    myquery = { 
            "user_id":userid , 
            "cur_weight":weight ,
            "start_date":day, 
            "start_month":month, 
            "date":{} , 
            "minutes":{} ,
            "cal_burnt":{} ,
            "total_min":0 , 
            "total_cal":0,
            "minutes_whole":0,
            "calories_whole":0
            }
    mycol.insert_one(myquery)    

def updateUserActivity(userid , minutes):
    entity_no = 1
    myuser = { "user_id" :userid}
    
    for x in mycol.find( {"user_id":userid} , {"start_date":1,"_id":0} ):
        pass
    for sd in x.values():
        pass
    x.clear()
    for x in mycol.find( {"user_id":userid} , {"start_month":1,"_id":0} ):
        pass
    for sm in x.values():
        pass
    x.clear()

    d=date.today()    
    if (sm==d.month or (sm!=d.month and d.date<sd)) :
        #date
        d=date.today()
        dd="{}/{}/{}".format(d.day,d.month,d.year)
        for x in mycol.find( {"user_id":userid} , {"date":1,"_id":0} ):
            pass
        for y in x.values():
            pass
        for z in y.values():
            entity_no = entity_no + 1
        y.update({"{}".format(entity_no) :dd})
        newquery = { "$set": { "date":y} }
        mycol.update_one(myuser,newquery)
        x.clear()
        y.clear()
        
        #minutes
        for x in mycol.find( {"user_id":userid} , {"minutes":1,"_id":0} ):
            pass
        for y in x.values():
            pass
        y.update({"{}".format(entity_no) :minutes})
        newquery = { "$set": { "minutes":y} }
        mycol.update_one(myuser,newquery)
        x.clear()
        
        #cur_weight
        for x in mycol.find( {"user_id":userid} , {"cur_weight":1,"_id":0} ):
            pass
        for w in x.values():
            pass
        hour = minutes/60
        cal = 3.3*w*hour
        x.clear()
        for x in mycol.find( {"user_id":userid} , {"cal_burnt":1,"_id":0} ):
            pass
        for y in x.values():
            pass
        y.update({"{}".format(entity_no) :cal})
        newquery = { "$set": { "cal_burnt":y} }
        mycol.update_one(myuser,newquery)
        x.clear()
            
        #total_min
        for x in mycol.find( {"user_id":userid} , {"total_min":1,"_id":0} ):
            pass
        for tm in x.values():
            pass
        newquery = { "$set": { "total_min": tm+minutes} }
        mycol.update_one(myuser,newquery)
        x.clear()
            
        #total_cal
        for x in mycol.find( {"user_id":userid} , {"total_cal":1,"_id":0} ):
            pass
        for tc in x.values():
            pass
        newquery = { "$set": { "total_cal": tc+cal} }
        mycol.update_one(myuser,newquery)
        x.clear()
        
    else:
        entity_no = 1
        add_cal = add_min = 0
        d=date.today()
        for x in mycol.find( {"user_id":userid} , {"cur_weight":1,"_id":0} ):
            pass
        for w in x.values():
            pass
        hour = minutes/60
        cal = 3.3*w*hour
        dd="{}/{}/{}".format(d.day,d.month,d.year)
        for x in mycol.find( {"user_id":userid} , {"total_cal":1,"caloies_whole":1,"_id":0} ):
            pass
        for ct in x.values():
            add_cal = add_cal + ct
        x.clear()
        for x in mycol.find( {"user_id":userid} , {"total_min":1,"minutes_whole":1, "_id":0} ):
            pass
        for mt in x.values():
            add_min = add_min + mt
        newquery = { "$set": { 
                                "start_date":d.day, 
                                "start_month":d.month,
                                "date": {"{}".format(entity_no) :dd} , 
                                "minutes":{"{}".format(entity_no) :minutes} , 
                                "cal_burnt":{"{}".format(entity_no) :cal} , 
                                "total_min":minutes , 
                                "total_cal":cal,
                                "minutes_whole":add_min,
                                "calories_whole":add_cal
                        } }
        mycol.update_one(myuser,newquery)
        
        