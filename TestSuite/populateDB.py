import pyrebase 

def main(db, userToken):
	#Patients
	db.child("patients").child("0").child("name").set("Eva", userToken)
	#Actuators
	db.child("actuators").child("0").child("name").set("Heater", userToken)
	#Rules
	db.child("rules").child("0").child("name").set("Temperature above 20C", userToken)
	db.child("rules").child("0").child("sensor").set("0", userToken)
	db.child("rules").child("0").child("value").set("20", userToken)
	db.child("rules").child("0").child("comparison").set("<", userToken)
	db.child("rules").child("0").child("actuator").set("0", userToken)
	db.child("rules").child("0").child("action").set("1", userToken)
	#Sensor
	db.child("actuators").child("0").child("name").set("Room Temperature", userToken)
	db.child("actuators").child("0").child("units").set("Celcius", userToken)
	#Sensor Data
	db.child("sensorData0").child("1709836639").child("value").set("19", userToken)