import modules.variables as v

def finderror():
	diff1=v.diff1
	diff2=v.diff2
	o2=v.o2
	a=max(diff1[2],diff1[5],diff1[10],diff1[12],diff1[1],diff1[4],diff1[13])
	x=diff1.index(a)
	
	if(x==2):
		if(o2[x]>170 and o2[x]<190):
			return "straighten right elbow"
		else:
			if((o2[x]>180 and diff2[x]>0) or (o2[x]<180 and diff2[x]<0)):
				return "straighten right elbow"
			else:
				return "bend right elbow"
	elif(x==5):
		if(o2[x]>170 and o2[x]<190):
			return "straighten left elbow"
		else:
			if((o2[x]>180 and diff2[x]>0) or (o2[x]<180 and diff2[x]<0)):
				return "straighten left elbow"
			else:
				return "bend left elbow"
	elif(x==10):
		if(o2[x]>170 and o2[x]<190):
			return "straighten right knee"
		else:
			if((o2[x]>180 and diff2[x]>0) or (o2[x]<180 and diff2[x]<0)):
				return "straighten right knee"
			else:
				return "bend right knee"
	elif(x==12):
		if(o2[x]>170 and o2[x]<190):
			return "straighten left knee"
		else:
			if((o2[x]>180 and diff2[x]>0) or (o2[x]<180 and diff2[x]<0)):
				return "straighten left knee"
			else:
				return "bend left knee"
	elif(x==1):
		if(diff2[x]<0):
			return "drop right hand"
		else:
			return "lift right hand"
	elif(x==4):
		if(diff2[x]<0):
			return "drop left hand"
		else:
			return "lift left hand"
	elif(x==13):
		if((o2[x]>180 and diff2[x]>0) or (o2[x]<180 and diff2[x]<0)):
			return "widen your stance"
		else:
			return "bring your feet closer too each other"