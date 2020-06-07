import OpenPoseImage as opi
import capture

o1=[]
o2=[]
diff=[]

capture.captureImage()

opi.OpenImage(o1,"new_image.jpeg","Output-Keypoints.jpg","Output-Skeleton.jpg")
opi.OpenImage(o2,"v1.jpg","Output-Keypoints1.jpg","Output-Skeleton1.jpg")

for i in range(len(o1)):
	if o1[i]!=0 and o2[i]!=0:
		diff.append(abs(o1[i]-o2[i]))	


print(o1)
print(o2)
print(diff)
print(sum(diff)/len(diff))
