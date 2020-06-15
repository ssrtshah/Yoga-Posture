import firebase


config = {
  	'apiKey': "AIzaSyCMspprnQ4tOwDHL-DBhqhdkX8xM8SwOqU",
    'authDomain': "yoga-posture-e5cdb.firebaseapp.com",
    'databaseURL': "https://yoga-posture-e5cdb.firebaseio.com",
    'projectId': "yoga-posture-e5cdb",
    'storageBucket': "yoga-posture-e5cdb.appspot.com",
    'messagingSenderId': "649842810638",
    'appId': "1:649842810638:web:7c45a9b58c8a92dfb9815f",
    'measurementId': "G-N6574YK0PW"
}

fb = firebase.Firebase(config)

storage = fb.storage()

storage.child("a1.jpg").download("new_image.jpg")
