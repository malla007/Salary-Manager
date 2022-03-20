import pyrebase
config = {
    "apiKey": "AIzaSyDYlfpxAvq14bqTnlrmVKw7YrJcyXMACOc",
    "authDomain": "salary-pir.firebaseapp.com",
    "databaseURL": "https://salary-pir.firebaseio.com",
    "projectId": "salary-pir",
    "storageBucket": "salary-pir.appspot.com",
    "messagingSenderId": "585545884380",
    "appId": "1:585545884380:web:82c838a49bb436294f8a19",
    "measurementId": "G-PKJ1MZVKJ1"
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()

email = input("Enter Email\n")
password = input("Enter Password\n")

user = auth.create_user_with_email_and_password(email,password)

auth.get_account_info(user['idToken'])
