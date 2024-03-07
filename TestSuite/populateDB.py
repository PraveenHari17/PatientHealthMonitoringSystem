import pyrebase 

def main(db, userToken):
	id = 100
	#Patients
	db.child("patients").child(id).child("name").set("Eva", userToken)
	#Actuators
	db.child("actuators").child(id).child("name").set("Heater", userToken)
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