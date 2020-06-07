import cv2
import time
import numpy as np
import angle as ag

def OpenImage(anglearr,ifile,ofile1,ofile2):
	protoFile = "pose/mpi/pose_deploy_linevec_faster_4_stages.prototxt"
	weightsFile = "pose/mpi/pose_iter_160000.caffemodel"
	nPoints = 15
	POSE_PAIRS = [[0,1], [1,2], [2,3], [3,4], [1,5], [5,6], [6,7], [1,14], [14,8], [8,9], [9,10], [14,11], [11,12], [12,13] ]

	ANGLE_POINTS = [[0,1,2],[1,2,3],[2,3,4],[0,1,5],[1,5,6],[5,6,7],[2,1,14],[1,14,8],[1,14,11],[14,8,9],[8,9,10],[14,11,12],[11,12,13]]

	frame = cv2.imread(ifile)
	frameCopy = np.copy(frame)
	frameWidth = frame.shape[1]
	frameHeight = frame.shape[0]
	threshold = 0.1

	net = cv2.dnn.readNetFromCaffe(protoFile, weightsFile)

	t = time.time()
	# input image dimensions for the network
	inWidth = 368
	inHeight = 368
	inpBlob = cv2.dnn.blobFromImage(frame, 1.0 / 255, (inWidth, inHeight),
	                          (0, 0, 0), swapRB=False, crop=False)

	net.setInput(inpBlob)

	output = net.forward()
	print("time taken by network : {:.3f}".format(time.time() - t))

	H = output.shape[2]
	W = output.shape[3]

	# Empty list to store the detected keypoints
	points = []

	for i in range(nPoints):
	    # confidence map of corresponding body's part.
	    probMap = output[0, i, :, :]

	    # Find global maxima of the probMap.
	    minVal, prob, minLoc, point = cv2.minMaxLoc(probMap)
	    
	    # Scale the point to fit on the original image
	    x = (frameWidth * point[0]) / W
	    y = (frameHeight * point[1]) / H

	    if prob > threshold : 
	        cv2.circle(frameCopy, (int(x), int(y)), 8, (0, 255, 255), thickness=-1, lineType=cv2.FILLED)
	        cv2.putText(frameCopy, "{}".format(i), (int(x), int(y)), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, lineType=cv2.LINE_AA)

	        # Add the point to the list if the probability is greater than the threshold
	        points.append((int(x), int(y)))
	    else :
	        points.append(None)

	# Draw Skeleton
	for pair in POSE_PAIRS:
	    partA = pair[0]
	    partB = pair[1]

	    if points[partA] and points[partB]:
	        cv2.line(frame, points[partA], points[partB], (0, 255, 255), 2)
	        cv2.circle(frame, points[partA], 8, (0, 0, 255), thickness=-1, lineType=cv2.FILLED)
	        cv2.circle(frame, points[partB], 8, (0, 0, 255), thickness=-1, lineType=cv2.FILLED)

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


	cv2.imshow('Output-Keypoints', frameCopy)
	cv2.imshow('Output-Skeleton', frame)


	cv2.imwrite(ofile1, frameCopy)
	cv2.imwrite(ofile2, frame)

	print("Total time taken : {:.3f}".format(time.time() - t))
