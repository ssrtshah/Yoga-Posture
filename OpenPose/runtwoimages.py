import OpenPoseImage as opi

o1=[]
o2=[]

opi.OpenImage(o1,"v1.jpg","Output-Keypoints.jpg","Output-Skeleton.jpg")
opi.OpenImage(o2,"v2.jpg","Output-Keypoints1.jpg","Output-Skeleton1.jpg")


print(o1)
print(o2)