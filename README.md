# Yoga-Posture

Befor running the code, download the file from this link and add it to pose/mpi
http://posefs1.perception.cs.cmu.edu/OpenPose/models/pose/mpi/pose_iter_160000.caffemodel

Modules required:

opencv-python, dnspython, python-jwt, sseclient, requests-toolbelt, pycryptodome, pymongo
(If you get an error saying Crypto module not found, go to the location where crypto module is installed and change the name of the folder and all subfolder with the first letter ad capital ie. crypto=>Crypto, math=>Math etc) 

```
pip install opencv-python
pip install dnspython
pip install python-jwt
pip install sseclient
pip install requests-toolbelt
pip install pycryptodome
pip install pymongo
```

To test only the backend code with image from webcam, run tester1.py. It will capture an image from the webcam of the computer/laptop and compare it to the Virabhdrasana pose.
```
python tester1.py
```

To test the backend code with pre-existing image, run tester2.py and change the path of input image to the desired image.
```
python tester2.py
```

To run the code from frontend, run api.py, calls will be made to the backend from the frontend itself.
```
python api.py
```
Git clone the [Frontend repository](https://github.com/LekhaKarthik/yogi-app) using the following command:
```
git clone https://github.com/LekhaKarthik/yogi-app
```
