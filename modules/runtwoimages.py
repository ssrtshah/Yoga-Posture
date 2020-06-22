import modules.OpenPoseImage as opi
import modules.capture
import time
import modules.finderror as fe
import modules.getvalues as gv


'''o1=[]
o2=[]
diff1=[]
diff2=[]'''
asana='vidharbhasana'
avg=0

'''angle_list={'vidharbhasana':[259.2581864991609, 200.6668284692978, 188.65104796437717, 121.08028572315077, 161.62831342275172, 171.9052149822932, 289.13753117352195, 202.34131675883563, 153.86078929933709, 229.2842910732751, 111.67520468698005, 165.84745615332864, 173.18623633463903, 287.01669700208566],
				'adhomukhashavasana':[0, 79.50852298766841, 173.9275435927923, 0, 0, 0, 71.18287265724155, 207.1255354890795, 196.60154315750205, 64.54901881628368, 0, 69.69999837023524, 177.9878653347631, 0],
				'sukhasana':[236.64597424848324, 131.5612421634349, 217.2511400460823, 129.98688624496418, 221.26695149248062, 148.40441637223083, 303.35402575151676, 206.8109543003487, 161.565051177078, 224.75409687672928, 22.07943833569357, 129.50767544287257, 323.0513268748269, 343.1252108134483],
				'vrikshasana':[253.47208859422315, 283.5748408488916, 214.61524023057032, 112.46464680146372, 71.15760662475687, 151.14832385436029, 290.3888243058423, 193.8621869878094, 155.76943898018334, 154.72554405998838, 179.83011359947287, 174.23355156654446, 0.0, 0.0]}'''

'''o2=angle_list[asana]'''




def TakeAndCompare():
	time.sleep(5)
	capture.captureImage()
	o11=[]
	diff1=[]
	diff2=[]
	count=0

	opi.OpenImage(o11,"new_image.jpg","Output-Keypoints.jpg","Output-Skeleton.jpg")

	for i in range(len(o11)):
		if o11[i]!=0 and o2[i]!=0:
			diff1.append(abs(o11[i]-o2[i]))
			diff2.append(o11[i]-o2[i])
			count=count+1
		else:
			diff2.append(0)
			diff1.append(0)

	avgerr =sum(diff1)/count
	return o11,avgerr,diff1,diff2

o1,avg,diff1,diff2=TakeAndCompare()

'''print(o1)
print(o2)
print(diff1)
print(diff2)
print(avg)'''

while(avg>9):
	movement = fe.finderror(o1,diff1,diff2)
	print('\n'+movement+'\n')
	o1,avg,diff1,diff2=TakeAndCompare()
	#print(o1)
	#print(o2)
	#print(diff1)
	#print(diff2)
	#print(avg)

