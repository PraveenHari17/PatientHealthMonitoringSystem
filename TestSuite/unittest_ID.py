import json
import pyrebase
import auth
class TestActuatorComparison:
    def __init__(self, firebase_config, id_data):
        self.firebase = pyrebase.initialize_app(firebase_config)
        self.db = self.firebase.database()
        self.id_data = id_data

    def compare_with_database(self):
        try:
            # Read data from the database actuator table
            db_actuators = self.db.child("actuators").get().val()
            if db_actuators is None:
                return False

            # Compare data
            return self.id_data == db_actuators

        except Exception as e:
            print("Error comparing data:", e)
            return False

# Firebase configuration
firebase = pyrebase.initialize_app(credentials.config) 
# Get a reference to the auth service
auth = firebase.auth()
# Log the user in
userToken = auth.sign_in_with_email_and_password(credentials.username, credentials.password)
db = firebase.database()



# Read data from the ID text file
with open('ID.txt', 'r') as file:
    id_data = json.load(file)

# Create an instance of the test case and run the test
test = TestActuatorComparison(firebase_config, id_data)
result = test.compare_with_database()

print("Test result:", result)

