import OpenPoseImage as opi

a1=[]
a2=[]
a3=[]
b1=[]
c1=[]
d1=[]
d2=[]
e1=[]
f1=[]
g1=[]
h1=[]
h2=[]
aavg=[]
davg=[]
havg=[]

f=open("image values.txt",'a')

opi.OpenImage(a1,"images/a1.jpg","images/a1-Keypoints.jpg","images/a1-Skeleton.jpg")
opi.OpenImage(a2,"images/a2.jpg","images/a2-Keypoints.jpg","images/a2-Skeleton.jpg")
opi.OpenImage(a3,"images/a3.jpg","images/a3-Keypoints.jpg","images/a3-Skeleton.jpg")
opi.OpenImage(b1,"images/b1.jpg","images/b1-Keypoints.jpg","images/b1-Skeleton.jpg")
opi.OpenImage(c1,"images/c1.jpg","images/c1-Keypoints.jpg","images/c1-Skeleton.jpg")
opi.OpenImage(d1,"images/d1.jpg","images/d1-Keypoints.jpg","images/d1-Skeleton.jpg")
opi.OpenImage(d2,"images/d2.jpg","images/d2-Keypoints.jpg","images/d2-Skeleton.jpg")
opi.OpenImage(e1,"images/e1.jpg","images/e1-Keypoints.jpg","images/e1-Skeleton.jpg")
opi.OpenImage(f1,"images/f1.jpg","images/f1-Keypoints.jpg","images/f1-Skeleton.jpg")
opi.OpenImage(g1,"images/g1.jpg","images/g1-Keypoints.jpg","images/g1-Skeleton.jpg")
opi.OpenImage(h1,"images/h1.jpg","images/h1-Keypoints.jpg","images/h1-Skeleton.jpg")
opi.OpenImage(h2,"images/h2.jpg","images/h2-Keypoints.jpg","images/h2-Skeleton.jpg")


for i in range(len(a1)):
	avg=(a1[i]+a2[i]+a3[i])/3
	aavg.append(avg)

for i in range(len(a1)):
	avg=(d1[i]+d2[i])/2
	davg.append(avg)

for i in range(len(a1)):
	avg=(h1[i]+h2[i])/2
	havg.append(avg)

f.write(str(aavg)+"\n"+"\n")
f.write(str(b1)+"\n"+"\n")
f.write(str(c1)+"\n"+"\n")
f.write(str(davg)+"\n"+"\n")
f.write(str(e1)+"\n"+"\n")
f.write(str(f1)+"\n"+"\n")
f.write(str(g1)+"\n"+"\n")
f.write(str(havg)+"\n"+"\n")