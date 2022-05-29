import pyrebase

def fire():
    firebaseConfig = {
    'apiKey': "AIzaSyA1AtXyKK5xKHEnfYQgpyAb4ar3EQEYyGc",
    'authDomain': "login-test-697b1.firebaseapp.com",
    'databaseURL': "https://login-test-697b1-default-rtdb.firebaseio.com",
    'projectId': "login-test-697b1",
    'storageBucket': "login-test-697b1.appspot.com",
    'messagingSenderId': "604903299923",
    'appId': "1:604903299923:web:76b2f8c9c9353782ca9fa6",
    'measurementId': "G-9HT2LHBV4T"
    };
        
    firebase = pyrebase.initialize_app(firebaseConfig) 
    return firebase
    