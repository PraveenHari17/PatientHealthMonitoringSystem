import pyrebase

credentials = {
     "config": {
         "apiKey": "AIzaSyCeiTiw7s57uVnVO_11P09zN54AOC12bjs",
         "authDomain": "sysc-l2-g5-project.firebaseapp.com",
         "databaseURL": "https://sysc-l2-g5-project-default-rtdb.firebaseio.com/",
         "storageBucket": "sysc-l2-g5-project.appspot.com",

     },
     "username": "sensornode@sysc3010project.com",
     "password": "sensorNode"
 }
def auth():
	# Init
	firebase = pyrebase.initialize_app(credentials["config"])
	# Get a reference to the auth service
	auth = firebase.auth()
	# Log the user in
	userToken = auth.sign_in_with_email_and_password(credentials["username"], credentials["password"])
	db = firebase.database()
	return (db, userToken)

db, userToken = auth()
if db:
    print("your're in")


# Define the rule to be written
rule_name = "Praveen"
rule_value = "Hello Aryan!"

# Construct the rule in a dictionary format
rule = {
    rule_name: rule_value
}

# Write the rule to the database
db.child("rules").child("100").set(rule, userToken)

print("Rule created successfully: " + rule_name + ": " + rule_value)
