# Yoga-Posture

Befor running the code, download the file from this link and add it to pose/mpi
(http://posefs1.perception.cs.cmu.edu/OpenPose/models/pose/mpi/pose_iter_160000.caffemodel)

Modules to install:
opencv-python, dnspython, python-jwt, sseclient, requests-toolbelt, pycryptodome, pymongo
(If you get an error saying Crpto module not found, go to the location where crpto module is installed and change the name of the folder and all subfolder with the first letter ad capital ie. crypto=>Crypto, math=>Math etc) 
[pip install opencv-python]
[pip install dnspython]


To test only the backend code with image from webcam, run tester1.py. It will capture an image from the webcam of the computer/laptop and compare it to the Virabhdrasana pose.
[python tester1.py]

To test the backend code with pre-existing image, run tester2.py and change the path of input image to the desired image.
[python tester2.py]

To run the code from frontend, run api.py, calls will be made to the backend from the frontend itself.
[python api.py]
