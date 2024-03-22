import unittest
from app import app  # Import your Flask app

class SensorDataTestCase(unittest.TestCase):
    
    def setUp(self):
        # Set up the app to work in testing mode
        app.testing = True
        self.app = app.test_client()
    
    def test_latest_sensor_data(self):
        # Make a GET request to the sensor data endpoint
        response = self.app.get('/latest-sensor-data')
        
        # Check if the status code of the response is OK (200)
        self.assertEqual(response.status_code, 200)
        
        # Load the response data as JSON
        data = response.get_json()

        # Assert that the required fields are in the data
        self.assertIn('Temperature', data)
        self.assertIn('Humidity', data)
        self.assertIn('Pressure', data)

        # Optionally, you can also assert the types of the values
        self.assertIsInstance(data['Temperature'], float)
        self.assertIsInstance(data['Humidity'], float)
        self.assertIsInstance(data['Pressure'], float)

if __name__ == '__main__':
    unittest.main()
