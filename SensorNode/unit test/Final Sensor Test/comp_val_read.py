import time
import board
import max30100
import adafruit_sht31d
import adafruit_bh1750
import pyrebase  
import time
from datetime import datetime

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
dataset_SPO2 = "SPO2data"
dataset_Light = "Lightdata"
username = "Atharva"

"""
#uncomment for running SPO2
#spo2 sensor config
oxy_sensor = max30100.MAX30100()
oxy_sensor.enable_spo2()
hb = 0#pulse initial value
spo2 = 0#oxygen initial value
"""

#Light sensor config
i2c_light = board.I2C()  # uses board.SCL and board.SDA
# i2c = board.STEMMA_I2C()  # For using the built-in STEMMA QT connector on a microcontroller
light_sensor = adafruit_bh1750.BH1750(i2c_light)
light_sensor_val = 0#initial value for light

# Create the I2C bus for temperature and humidity sensor
i2c_temp_humi = board.I2C()
# Create a sensor instance
temp_humi_sensor = adafruit_sht31d.SHT31D(i2c_temp_humi, address=0x45)

#write spo2 data to database
def writeSPO2Data(pulse,spo2):
            
    sensorData = f"SPO2: {spo2}, pulse: {pulse}"
        
    # Generate a timestamp (Unix timestamp in milliseconds)
    #timestamp = int((datetime.now().timestamp()) * 1000)
    timestamp = f"{datetime.now():%Y-%m-%d %H-%M-%S}"
        
    # When writing to your DB each child is a JSON key:value pair
    #db.child(username).child(dataset_SPO2).child(timestamp).set(sensorData)
    db.child("sensorData103").child(timestamp).set(sensorData)
    # The above command will add a JSON string to your DB in the form:
    # {
    #   "YOUR_USERNAME":{
    #     "SPO2data":{
    #       "<timestamp>":"<sensor values>"
    #     }
    #   }
    # }

    #count += 1

def spo2_sensor_val():
    oxy_sensor.read_sensor()

    oxy_sensor.ir, oxy_sensor.red

    hb = int(oxy_sensor.ir / 100)
    spo2 = int(oxy_sensor.red / 100)
    
    if oxy_sensor.ir != oxy_sensor.buffer_ir :
        print("Pulse:",hb);
    if oxy_sensor.red != oxy_sensor.buffer_red:
        print("SPO2:",spo2);

def SPO2_helper():
    spo2_sensor_val()
    writeSPO2Data(hb,spo2)


#write spo2 data to database
def writeLightData(val):
            
    sensorData = f"Light (LUX): {val}"
        
    # Generate a timestamp (Unix timestamp in milliseconds)
    #timestamp = int((datetime.now().timestamp()) * 1000)
    timestamp = f"{datetime.now():%Y-%m-%d %H-%M-%S}"
        
    # When writing to your DB each child is a JSON key:value pair
    #db.child(username).child(dataset_Light).child(timestamp).set(sensorData)
    db.child("sensorData101").child(timestamp).set(sensorData)

    # The above command will add a JSON string to your DB in the form:
    # {
    #   "YOUR_USERNAME":{
    #     "Lightdata":{
    #       "<timestamp>":"<sensor values>"
    #     }
    #   }
    # }
def light_sensor_val():
    light_sensor_val = light_sensor.lux
    writeLightData(light_sensor_val)
    print("%.2f Lux" % light_sensor_val)

def light_helper():
    light_sensor_val()

def writetemphumidity(humi,room_temp):
    tempSensorData = f"Temperature: {room_temp:.2f} degrees C"
    humiSensorData = f"Humidity: {humi:.2f} %"   
    
    # Generate a timestamp (Unix timestamp in milliseconds)
    #timestamp = int((datetime.now().timestamp()) * 1000)
    timestamp = f"{datetime.now():%Y-%m-%d %H-%M-%S}"
        
    # When writing to your DB each child is a JSON key:value pair
    #db.child(username).child(dataset_Light).child(timestamp).set(sensorData)
    db.child("sensorData102").child(timestamp).set(humiSensorData)
    db.child("sensorData100").child(timestamp).set(tempSensorData)

def temp_humidity_sensor_val():
    humidity_sensor_val = temp_humi_sensor.humidity
    room_temp_sensor_val = temp_humi_sensor.temperature
    writeLightData(humidity_sensor_val, room_temp_sensor_val)
    print('Temperature: {:.2f} degrees C'.format(room_temp_sensor_val))
    print('Humidity: {:.2f}%'.format(humidity_sensor_val))
    
def temp_humidity_helper():
    temp_humidity_sensor_val()
"""
while 1:
    #SPO2_helper()
    #light_helper()
    temp_humidity_helper()
    time.sleep(3)
"""
"""
writetemphumidity(55.66678,27)
writeLightData(6000)
writeSPO2Data(65,95)
"""