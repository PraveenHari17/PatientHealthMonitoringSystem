from flask import Flask, request, jsonify, render_template
import pyrebase
from uuid import uuid4

app = Flask(__name__)

# Firebase configuration
firebaseConfig = {
    "apiKey": "AIzaSyCeiTiw7s57uVnVO_11P09zN54AOC12bjs",
    "authDomain": "sysc-l2-g5-project.firebaseapp.com",
    "databaseURL": "https://sysc-l2-g5-project-default-rtdb.firebaseio.com/",
    "storageBucket": "sysc-l2-g5-project.appspot.com",
}

# Initialize Firebase
firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
db = firebase.database()
user = auth.sign_in_with_email_and_password("sensornode@sysc3010project.com", "sensorNode")
userToken = user['idToken']

# Route to serve the index.html page
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/latest-sensor-data')
def latest_sensor_data():
    # Initialize a dictionary to hold the sensor data
    sensor_data = {
        "Temperature": None,
        "Light": None,
        "Humidity": None,
        "BloodOxygen": None,
        "HeartRate": None,
        "BodyTemperature": None
    }

    # Define the keys for sensor data in Firebase
    sensor_keys = {
        "0": "Temperature",
        "1": "Light",
        "2": "Humidity",
        "3": "BloodOxygen",
        "4": "HeartRate",
        "5": "BodyTemperature"
    }

    # Retrieve and store the latest value for each sensor
    for key, value in sensor_keys.items():
        latest_entry = db.child(f"sensorData{key}").order_by_key().limit_to_last(1).get().val()
        if latest_entry:
            # Extract the value from the latest entry dictionary
            last_entry_key = next(iter(latest_entry))
            sensor_data[value] = latest_entry[last_entry_key]["value"]

    return jsonify(sensor_data)
    
@app.route('/submit-rule', methods=['POST'])
def submit_rule():
    data = request.get_json()
    rules = db.child("rules").get(userToken).val()

    # If rules is None, it means there are no rules yet
    if not rules:
        next_id = '0'
    else:
        # If rules is a list, the next ID should be the length of this list
        if isinstance(rules, list):
            next_id = str(len(rules))
        else:
            # If rules is a dictionary, extract IDs and find the next one
            rule_ids = [int(k) for k in rules.keys()]
            next_id = str(max(rule_ids) + 1)
    # Create the rule object
    rule = {
        'name': data['name'],
        'action': data['action'],
        'actuator': data['actuator'],
        'comparison': data['comparison'],
        'sensor': data['sensor'],
        'value': data['value']
    }
    
    # Write the rule to Firebase
    db.child("rules").child(next_id).set(rule, userToken)
    
    return jsonify({"success": True, "rule_id": next_id}), 200


@app.route('/server-status')
def server_status():
    return jsonify(status='alive'), 200


if __name__ == '__main__':
    app.run(debug=True, port=5001)
