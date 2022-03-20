import pyrebase
config = {

}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()

email = input("Enter Email\n")
password = input("Enter Password\n")

user = auth.create_user_with_email_and_password(email,password)

auth.get_account_info(user['idToken'])
