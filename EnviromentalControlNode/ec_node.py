import json 
import RPi.GPIO as GPIO
from time import sleep
import pyrebase
"""
Use this when you need to check the ID files
with open('ID.txt', 'r') as file:
    file_contents = file.read()

ID_json = file_contents.split('\n')

print(ID_json)
"""
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

def initialize_value_uT(db, userToken):
	ids = ["100", "101", "102"]
	data_to_set = [{ 
	        "id": 100,
	            "name": "Heater",
	            "unit": "Celcius"
	          },
		  {
		    "id": 101,
		    "name": "Light",
		    "unit": "Lux"
		  },
		  {
		    "id": 102,
		    "name": "Fans",
		    "unit": "RPM"
		    }
		  ]
	#Actuators
	db.child("actuators").set(data_to_set)
	
initialize_value_uT(db, userToken)



GPIO.setmode(GPIO.BCM)

def heater(state):
    gpio_pin = 17
    # Set up the GPIO pin as an output
    GPIO.setup(gpio_pin, GPIO.OUT)
    if state == "on":
        GPIO.output(gpio_pin, GPIO.HIGH)
        print("GPIO pin {} is turned ON.".format(gpio_pin))
    if state == "off":
        GPIO.output(gpio_pin, GPIO.LOW)
        print("GPIO pin {} is turned OFF.".format(gpio_pin))

def light(state):
    gpio_pin = 19
    # Set up the GPIO pin as an output
    GPIO.setup(gpio_pin, GPIO.OUT)
    if state == "on":
        GPIO.output(gpio_pin, GPIO.HIGH)
        print("GPIO pin {} is turned ON.".format(gpio_pin))
    if state == "off":
        GPIO.output(gpio_pin, GPIO.LOW)
        print("GPIO pin {} is turned OFF.".format(gpio_pin))
        
def fans(state):
    gpio_pin = 12
    GPIO.setup(gpio_pin, GPIO.OUT)
    if state == "on":
        GPIO.output(gpio_pin, GPIO.HIGH)
        print("GPIO pin {} is turned ON.".format(gpio_pin))
    if state == "off":
        GPIO.output(gpio_pin, GPIO.LOW)
        print("GPIO pin {} is turned OFF.".format(gpio_pin))




logic_operators = {"<": lambda a, b: a < b,
               ">": lambda a, b: a > b,
               "==": lambda a, b: a == b,
               "<=": lambda a, b: a <= b,
                   ">=": lambda a, b: a >= b
              }
def check_sensor_data(parent_node):
    data_dict = {}
# Read data from the parent node
    parent_data = db.child(parent_node).get().val()
    if parent_data is not None:
    # Iterate over each child node
        for node_key, node_value in parent_data.items():
            print("Node:", node_key)
            data_dict[node_key] = node_value
            print("Value:", node_value)
        
    else:
        print("Parent node", parent_node, "does not exist.")
        
    return data_dict

def get_table_data(your_table_path):
    # Retrieve table data from Firebase
    table_data = db.child(your_table_path).get().val()
    return table_data


def ecn_node():
    rules_data = get_table_data("rules")
    for rule_id, rule_info in rules_data.items():
        # Skip non-rule entries
        if isinstance(rule_info, str):
            continue
        action = rule_info["action"]
        actuator = rule_info["actuator"]
        comparison = rule_info["comparison"]
        name = rule_info["name"]
        sensor = rule_info["sensor"]
        value = rule_info["value"]
        sensor_table =""
        
        if sensor == "0":
            sensor_table = get_table_data("sensorData100")
        elif sensor == "1":
            sensor_table = get_table_data("sensorData101")
        elif sensor == "2":
            sensor_table = get_table_data("sensorData102")
            
            
        for time_id, sensor_info in sensor_table.items():
            if logic_operators[comparison](value, sensor_info["value"]):
                if action == "1":
                    if actuator == "0":
                        print("Turned on")
                        heater("on")
                    elif actuator == "1":
                        light("on")
                        print("Turned on")
                    elif actuator == "2":
                        fans("on")
                        print("Turned on")
                if action == "0":
                    if actuator == "0":
                        heater("off")
                        print("Turned off")
                    elif actuator == "1":
                        light("off")
                        print("Turned off")
                    elif actuator == "2":
                        fans("off")
                        print("Turned off")
                
                
        
    
ecn_node()
        
        
        
            


