import unittest
from app import app  

class ServerStatusTestCase(unittest.TestCase):
    
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_server_status(self):
        
        response = self.app.get('/server-status')
        
        # Check if the response status code is 200
        self.assertEqual(response.status_code, 200)
        
        
        status = response.get_json().get('status')
        self.assertEqual(status, 'alive')

# This allows the test to be run from the command line
if __name__ == '__main__':
    unittest.main()
