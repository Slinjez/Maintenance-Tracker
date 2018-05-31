'''the tests should cover 
1. when the request is missing
'''
import unittest
import requests
import json
import sys


class TestGetSingleUserRequest(unittest.TestCase):
    requestoutarange = {
        "requestid": 8
    }
    
    def test_missing_request(self):        
        headers = {'content-type': 'application/json'}
        result = requests.get('http://127.0.0.1:5000/api/v1/users/request/',
                               data=json.dumps(self.requestoutarange), headers=headers)
        #assert result.status_code == 200
        self.assertEqual(result.json(), {"response": "No requests for this user"})
    
    
    
    

if __name__ == '__main__':
    unittest.main()