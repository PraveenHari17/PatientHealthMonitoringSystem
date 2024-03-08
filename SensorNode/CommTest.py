import pyrebase  
import time
from sense_hat import SenseHat
from datetime import datetime

sense = SenseHat()

# Config contains the information needed to connect to team firebase 

config = {
    "apiKey": "AIzaSyCeiTiw7s57uVnVO_11P09zN54AOC12bjs",
    "authDomain": "sysc-l2-g5-project.firebaseapp.com",
    "databaseURL": "https://sysc-l2-g5-project-default-rtdb.firebaseio.com/",
    "storageBucket": "sysc-l2-g5-project.appspot.com"
}

# Connect using your configuration 
firebase = pyrebase.initialize_app(config) 
db = firebase.database() 
dataset = "sensordata"
username = "Atharva"

# Write 10 data entries to the DB in a loop
def writeData():
    #count = 0
    while (1):
    
        temperature = sense.get_temperature()
        humidity = sense.get_humidity()
        pressure = sense.get_pressure()
        
        sensorData = f"Temperature: {temperature},Pressure: {pressure},Humidity: {humidity}"
        
        # Generate a timestamp (Unix timestamp in milliseconds)
        #timestamp = int((datetime.now().timestamp()) * 1000)
        timestamp = f"{datetime.now():%Y-%m-%d %H-%M-%S}"
        
        # When writing to your DB each child is a JSON key:value pair
        db.child(username).child(dataset).child(timestamp).set(sensorData)

        # The above command will add a JSON string to your DB in the form:
        # {
        #   "YOUR_USERNAME":{
        #     "sensordata":{
        #       "<timestamp>":"<sensor values>"
        #     }
        #   }
        # }

        #count += 1
        time.sleep(3)

writeData()