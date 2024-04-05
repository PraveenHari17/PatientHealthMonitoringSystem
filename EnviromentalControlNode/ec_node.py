import json 
import RPi.GPIO as GPIO
from time import sleep
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

def initialize_value_uT(db, userToken):
    ids = ["0", "1", "2"]
    data_to_set = [{ 
        "name": "Heater",
    },
    {
        "name": "Light",
    },
    {
        "name": "Fans",
    }]
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
    for item in rules_data:
        print(item)
        action = item["action"]
        actuator = item["actuator"]
        comparison = item["comparison"]
        name = item["name"]
        sensor = item["sensor"]
        value = int(item["value"])
        if sensor == "0":
            sensor_table = db.child("sensorData0").get()
        elif sensor == "1":
            sensor_table = db.child("sensorData1").get()
        elif sensor == "2":
            sensor_table = db.child("sensorData2").get()
        elif sensor == "3":
            sensor_table = db.child("sensorData3").get()
        elif sensor == "4":
            sensor_table = db.child("sensorData4").get()
        elif sensor == "5":
            sensor_table = db.child("sensorData5").get()
        sensor_value = int(sensor_table.each()[-1].val()["value"])
        print(sensor_value)
        
        if logic_operators[comparison](sensor_value, value):
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
        else:
            if action == "0":
                if actuator == "0":
                    print("Turned on")
                    heater("on")
                elif actuator == "1":
                    light("on")
                    print("Turned on")
                elif actuator == "2":
                    fans("on")
                    print("Turned on")
            if action == "1":
                if actuator == "0":
                    heater("off")
                    print("Turned off")
                elif actuator == "1":
                    light("off")
                    print("Turned off")
                elif actuator == "2":
                    fans("off")
                    print("Turned off")

while True:
    ecn_node()
    sleep(5)
