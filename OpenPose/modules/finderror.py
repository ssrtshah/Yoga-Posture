import modules.variables as v

def finderror():
	diff1=v.diff1
	diff2=v.diff2
	o2=v.o2
	a=max(diff1[2],diff1[5],diff1[10],diff1[12],diff1[1],diff1[4],diff1[13])
	x=diff1.index(a)
	
	if(x==2):
		if(o2[x]>170 and o2[x]<190):
			return "1"
		else:
			if((o2[x]>180 and diff2[x]>0) or (o2[x]<180 and diff2[x]<0)):
				return "1"
			else:
				return "2"
	elif(x==5):
		if(o2[x]>170 and o2[x]<190):
			return "3"
		else:
			if((o2[x]>180 and diff2[x]>0) or (o2[x]<180 and diff2[x]<0)):
				return "3"
			else:
				return "4"
	elif(x==10):
		if(o2[x]>170 and o2[x]<190):
			return "5"
		else:
			if((o2[x]>180 and diff2[x]>0) or (o2[x]<180 and diff2[x]<0)):
				return "5"
			else:
				return "6"
	elif(x==12):
		if(o2[x]>170 and o2[x]<190):
			return "7"
		else:
			if((o2[x]>180 and diff2[x]>0) or (o2[x]<180 and diff2[x]<0)):
				return "7"
			else:
				return "8"
	elif(x==1):
		if(diff2[x]<0):
			return "9"
		else:
			return "20"
	elif(x==4):
		if(diff2[x]<0):
			return "11"
		else:
			return "12"
	elif(x==13):
		if((o2[x]>180 and diff2[x]>0) or (o2[x]<180 and diff2[x]<0)):
			return "13"
		else:
			return "14"