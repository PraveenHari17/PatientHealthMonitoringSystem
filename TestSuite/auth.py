import pyrebase 
import credentials

def auth():
	# Init
	firebase = pyrebase.initialize_app(credentials.config)
	# Get a reference to the auth service
	auth = firebase.auth()
	# Log the user in
	userToken = auth.sign_in_with_email_and_password(credentials.username, credentials.password)
	db = firebase.database()
	return (db, userToken)
