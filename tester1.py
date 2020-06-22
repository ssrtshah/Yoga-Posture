import runmain as rm
import modules.capture as capture
import time

d={'1':'straighten right elbow','2':'bend right elbow','3':'straighten left elbow','4':'bend left elbow','5':'straighten right knee','6':'bend right knee','7':'straighten left knee','8':'bend left knee','9':'drop right hand','10':'lift right hand','11':'drop left hand','12':'lift left hand','13':'widen your stance','14':'bring your feet closer too each other'}

rm.getvaluesfromdb('Virabhadrasana')
#5 seconds to move away from camear and get into the pose
time.sleep(5)
capture.captureImage()
print(rm.takeAndCompare())
x=rm.findingerror()
print(d[x])


