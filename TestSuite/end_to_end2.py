import pyrebase

credentials = {
     "config": {
         "apiKey": "AIzaSyCeiTiw7s57uVnVO_11P09zN54AOC12bjs",
         "authDomain": "sysc-l2-g5-project.firebaseapp.com",
         "databaseURL": "https://sysc-l2-g5-project-default-rtdb.firebaseio.com/",
         "storageBucket": "sysc-l2-g5-project.appspot.com",

     },
     "username": "ecn@sysc3010project.com",
     "password": "ECNECN"
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
# Function to read specific rules
def read_specific_rules(rule_name):
    # Get specific rule
	rule = db.child("rules").child("100").get(userToken)
	return rule.val()

# Call the function to read a specific rule
rule_name = "Praveen"
specific_rule = str(read_specific_rules(rule_name))

# Print the specific rule
print(specific_rule)
if specific_rule == "OrderedDict([('Praveen', 'Hello Aryan!')])":
	print("Test passed")
	exit (1)
else:
	exit(0)



