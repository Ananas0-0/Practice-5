import unittest
import requests
import json

class TestTimeEndpoint(unittest.TestCase):
    def test_time_not_zero(self):
        response = requests.get('http://localhost:5000/time')
        data = response.json()
        self.assertNotEqual(data['time'], 0)
        self.assertIsInstance(data['time'], int)

if __name__ == '__main__':
    unittest.main()