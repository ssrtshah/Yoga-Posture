def finderror(o2,x,diff2):
	
	if(x==2):
		if(o2[x]>173 and o2[x]<187):
			return "straighten right elbow"
		else:
			if((o2[x]>180 and diff2[x]>0) or (o2[x]<180 and diff2[x]<0)):
				return "straighten right elbow"
			else:
				return "bend right elbow"
	elif(x==5):
		if(o2[x]>173 and o2[x]<187):
			return "straighten left elbow"
		else:
			if((o2[x]>180 and diff2[x]>0) or (o2[x]<180 and diff2[x]<0)):
				return "straighten left elbow"
			else:
				return "bend left elbow"
	elif(x==10):
		if(o2[x]>173 and o2[x]<187):
			return "straighten right knee"
		else:
			if((o2[x]>180 and diff2[x]>0) or (o2[x]<180 and diff2[x]<0)):
				return "straighten right knee"
			else:
				return "bend right knee"
	elif(x==12):
		if(o2[x]>173 and o2[x]<187):
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