'''the tests should cover 
1. test non existing request
'''
import unittest
import requests
import json
import sys

class TestEditRequest(unittest.TestCase):
    request = {
        "requestid": 8
    }
    
    def test_unexisting_requestId(self,request):
        result = requests.post('http://127.0.0.1:5000//api/v1/users/requests/',data=json.dumps(request), content_type='application/json')
        assert result.status_code == 200
        self.assertEqual(result.json(), {"requests": "Cannot edit this requests"})
        
    
    

if __name__ == '__main__':
    unittest.main()