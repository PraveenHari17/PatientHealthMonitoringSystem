import pyrebase 
import credentials

def main(db, userToken):
	ids = ["100", "101", "102"]
	for id in ids:
		#Patients
		db.child("patients").child(id).child("name").set("Eva", userToken)
		#Actuators
		#Rules
		db.child("rules").child(id).child("name").set("Temperature above 20C", userToken)
		db.child("rules").child(id).child("sensor").set("0", userToken)
		db.child("rules").child(id).child("value").set("20", userToken)
		db.child("rules").child(id).child("comparison").set("<", userToken)
		db.child("rules").child(id).child("actuator").set("0", userToken)
		db.child("rules").child(id).child("action").set("1", userToken)
		#Sensor
		db.child("sensors").child(id).child("name").set("Room Temperature", userToken)
		db.child("sensors").child(id).child("units").set("Celcius", userToken)
		#Sensor Data
		db.child("sensorData"+id).child("1709836639").child("value").set("19", userToken)
	
    db.child("actuators").child(100).child("name").set("Heater", userToken)
    db.child("actuators").child(101).child("name").set("Light", userToken)
    db.child("actuators").child(102).child("name").set("Fans", userToken)
    
    

# Init
firebase = pyrebase.initialize_app(credentials.config) 

# Get a reference to the auth service
auth = firebase.auth()
# Log the user in
userToken = auth.sign_in_with_email_and_password(credentials.username, credentials.password)
db = firebase.database()

main(db, userToken)