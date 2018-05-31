'''the tests should cover 
1. when the request is missing
'''
import unittest
import requests
import json
import sys

class TestGetSingleUserRequest(unittest.TestCase):
    
    def test_missing_request(self):
        result = requests.get('http://127.0.0.1:5000/api/v1/users/request/3')
        self.assertEqual(
            result.json(), {"requests": "No requests for this user"})
    
    
    
    

if __name__ == '__main__':
    unittest.main()