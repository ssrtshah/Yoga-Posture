import OpenPoseImage as opi
import capture
import finderror as fe
import variables as v
import getvalues as gv


def getvaluesfromdb(asananame):
	v.asananame=asananame
	v.o2=gv.getvalues(asananame)


def takeAndCompare(imagename):
	o1=[]
	diff1=[]
	diff2=[]
	o2=v.o2

	asana=v.asananame
	count=0
	imagefile=imagename

	capture.captureImage()

	opi.OpenImage(o1,imagefile,"Output-Keypoints.jpg","Output-Skeleton.jpg")

	for i in range(len(o1)):
		if o1[i]!=0 and o2[i]!=0:
			diff1.append(abs(o1[i]-o2[i]))
			diff2.append(o1[i]-o2[i])
			count=count+1
		else:
			diff2.append(0)
			diff1.append(0)

	avgerr =sum(diff1)/count

	v.o1=o1
	v.diff1=diff1
	v.diff2=diff2
	v.avg=avgerr

	return avgerr

def findingerror():
	movement = fe.finderror()
	return movement


