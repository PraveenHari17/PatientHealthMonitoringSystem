import pyrebase 
import credentials

# Init
firebase = pyrebase.initialize_app(config) 
# Get a reference to the auth service
auth = firebase.auth()
# Log the user in
userToken = auth.sign_in_with_email_and_password(credentials.email, credentials.password)
db = firebase.database() 

