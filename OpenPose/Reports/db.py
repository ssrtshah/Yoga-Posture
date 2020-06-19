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
    for dic in mycol.find( {"user_id":userid} , {"date":1 , "minutes":1 , "cal_burnt":1 ,"_id":0} ):
        pass
    final = []
    for i in range(1 , len(dic['date'])+1):
        final.append({"Date":dic['date']['{}'.format(i)], "Duration":dic['minutes']['{}'.format(i)] , "Calories":dic['cal_burnt']['{}'.format(i)]})
    return final

def prevUserReport(userid , month):
    myuser = { "user_id" :userid}
    for x in mycol.find( {"user_id":userid} , {"month_record":1,"_id":0} ):
        pass
    for y in x.values():
        pass
    dic = y["{}".format(month)]
    final = []
    for i in range(1 , len(dic['date'])+1):
        final.append({"Date":dic['date']['{}'.format(i)], "Duration":dic['minutes']['{}'.format(i)] , "Calories":dic['cal_burnt']['{}'.format(i)]})
    return final

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
            "calories_whole":0 ,
            "month_record":{}
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
    if (sm==d.month or (sm!=d.month and d.day<sd)) :
        i=1
        d=date.today()
        for x in mycol.find( {"user_id":userid} , {"date":1,"_id":0} ):
            pass
        for y in x.values():
            pass
        for z in y.values():
            i=i+1
        if i!=1 and int(z[0:2]) == d.day :
            #minutes
            for x in mycol.find( {"user_id":userid} , {"minutes":1,"_id":0} ):
                pass
            for y in x.values():
                pass
            z=y[str(i-1)]
            y.update({"{}".format(i-1) :minutes+z})
            newquery = { "$set": { "minutes":y} }
            mycol.update_one(myuser,newquery)
            x.clear()
            
            #cal_burnt
            for x in mycol.find( {"user_id":userid} , {"cur_weight":1,"_id":0} ):
                pass
            for w in x.values():
                pass
            hr = minutes/60
            cal = 3.3*w*hr
            x.clear()
            for x in mycol.find( {"user_id":userid} , {"cal_burnt":1,"_id":0} ):
                pass
            for y in x.values():
                pass
            z=y[str(i-1)]
            y.update({"{}".format(i-1) :cal+z})
            newquery = { "$set": { "cal_burnt":y} }
            mycol.update_one(myuser,newquery)
            x.clear()
            
        else:
            #date
            dd="{}/{}/{}".format(d.day,d.month,d.year)
            #print(y)
            y.update({"{}".format(i) :dd})
            newquery = { "$set": { "date":y} }
            mycol.update_one(myuser,newquery)
            x.clear()
            y.clear()
        
            #minutes
            for x in mycol.find( {"user_id":userid} , {"minutes":1,"_id":0} ):
                pass
            for y in x.values():
                pass
            y.update({"{}".format(i) :minutes})
            newquery = { "$set": { "minutes":y} }
            mycol.update_one(myuser,newquery)
            x.clear()
            
            #cal_burnt
            for x in mycol.find( {"user_id":userid} , {"cur_weight":1,"_id":0} ):
                pass
            for w in x.values():
                pass
            hr = minutes/60
            cal = 3.3*w*hr
            for x in mycol.find( {"user_id":userid} , {"cal_burnt":1,"_id":0} ):
                pass
            for y in x.values():
                pass
            y.update({"{}".format(i) :cal})
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
        i=1
        #for x in mycol.find( {"user_id":userid} , {"date":1, "minutes":1, "cal_burnt":1,"total_min":1,"total_cal":1,"_id":0} ):
        for x in mycol.find( {"user_id":userid} , {"date":1, "minutes":1, "cal_burnt":1,"_id":0} ):
            pass
        for y in  mycol.find( {"user_id":userid}, {"month_record":1,"_id":0}):
            pass
        for z in y.values():
            pass
        for z1 in z.values():
            i=i+1
        z.update({"{}".format(i) :x})
        newquery = { "$set": { "month_record":z} }
        mycol.update_one(myuser,newquery)
        x.clear()
        y.clear()
        z.clear()

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
        for x in mycol.find( {"user_id":userid} , {"total_cal":1,"calories_whole":1,"_id":0} ):
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
        
def resetReport(userid):
    myuser = { "user_id" :userid}
    d=date.today()
    newquery = { "$set": { 
                                "start_date":d.day, 
                                "start_month":d.month,
                                "date":{} , 
                                "minutes":{} ,
                                "cal_burnt":{} ,
                                "total_min":0 , 
                                "total_cal":0,
                                "minutes_whole":0,
                                "calories_whole":0,
                                "month_record":{}
                        } }
    mycol.update_one(myuser,newquery)
