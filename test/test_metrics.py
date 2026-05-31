import unittest
import requests
import json

class TestMetricsEndpoint(unittest.TestCase):
    def setUp(self):
        self.base_url = "http://localhost:5000"

    def test_metrics_returns_count(self):
        # Сброс счётчика через несколько запросов
        requests.get(f"{self.base_url}/time")
        requests.get(f"{self.base_url}/time")
        
        response = requests.get(f"{self.base_url}/metrics")
        data = response.json()
        
        self.assertIn('count', data)
        self.assertEqual(data['count'], 2)

if __name__ == '__main__':
    unittest.main()