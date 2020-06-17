import angle as ag

j1=[(258, 292), (350, 281), (368, 302), (350, 354), (331, 438), (350, 240), (368, 166), (350, 93), (442, 292), (387, 375), (331, 438), (497, 271), (571, 375), (626, 459), (405, 281)]

j2=[(104, 136), (156, 150), (147, 176), (147, 215), (139, 254), (156, 123), (165, 78), (156, 32), (208, 163), (182, 215), (139, 254), (234, 143), (278, 202), (313, 254), (191, 150)]

j3=[(962, 830), (1236, 830), (1168, 949), (1168, 1146), (1099, 1384), (1236, 711), (1236, 593), (1305, 395), (1443, 949), (1374, 1186), (1099, 1423), (1580, 869), (1717, 1146), (1855, 1423), (1374, 869)]

k2=[(350, 0), (350, 46), (317, 84), (300, 150), (283, 206), (400, 75), (400, 131), (417, 187), (333, 197), (333, 300), (350, 403), (384, 197), (384, 291), (367, 403), (350, 140)]

k3=[(424, 17), (424, 104), (339, 173), (339, 278), (318, 400), (509, 173), (509, 295), (551, 400), (381, 400), (381, 573), (403, 730), (466, 400), (466, 556), (445, 730), (424, 278)]

ANGLE_POINTS = [[0,1,2],[1,2,3],[2,3,4],[0,1,5],[1,5,6],[5,6,7],[2,1,14],[1,14,8],[1,14,11],[14,8,9],[8,9,10],[14,11,12],[11,12,13],[10,14,13]]


def findangle(points):
	anglearr=[]
	for angle in range(len(ANGLE_POINTS)):
			p1 = ANGLE_POINTS[angle][0]
			p2 = ANGLE_POINTS[angle][1]
			p3 = ANGLE_POINTS[angle][2]

			if points[p1] and points[p2] and points[p3]:
				x = ag.getAngle(points[p1],points[p2],points[p3])
				anglearr.append(x)
			else:
				nullval=0
				anglearr.append(nullval)
	return anglearr


j11=findangle(j1)
j21=findangle(j2)
j31=findangle(j3)
k21=findangle(k2)
k31=findangle(k3)

javg=[]
kavg=[]

for i in range(len(k21)):
	avg=(k31[i]+k21[i])/2
	kavg.append(avg)

for i in range(len(j11)):
	avg=(j11[i]+j21[i]+j31[i])/3
	javg.append(avg)


f=open("anglelist.txt",'a')
f.write(str(javg)+'\n'+'\n')
f.write(str(kavg)+'\n'+'\n')


