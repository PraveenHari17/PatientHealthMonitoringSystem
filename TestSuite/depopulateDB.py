import pyrebase 
import credentials

def main(db, userToken):
	ids = ["100", "101", "102"]
	for id in ids:
		#Patients
		db.child("patients").child(id).remove(userToken)
		#Actuators
		db.child("actuators").child(id).remove(userToken)
		#Rules
		db.child("rules").child(id).remove(userToken)
		#Sensor
		db.child("sensors").child(id).remove(userToken)
		#Sensor Data
		db.child("sensorData"+id).remove(userToken)

# Init
firebase = pyrebase.initialize_app(credentials.config) 

# Get a reference to the auth service
auth = firebase.auth()
# Log the user in
userToken = auth.sign_in_with_email_and_password(credentials.username, credentials.password)
db = firebase.database()

main(db, userToken)