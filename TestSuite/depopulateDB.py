import pyrebase 

def main(db, userToken):
	ids = [100, 101, 102]
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