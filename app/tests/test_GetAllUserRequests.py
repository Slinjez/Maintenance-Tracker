'''the tests should cover 
1. when user has no requests
2. test for request without user id
'''
import unittest
import requests
import json
import sys
#from ../../app.py import app #failed

class TestGetAllUserRequests(unittest.TestCase):
    
    def test_client_with_no_request(self):
        result = requests.get('http://127.0.0.1:5000/maintenance_tracker/api/v1/getAllRequests/3')
        self.assertEqual(result.json(),{"requests":"No requests for this user"})
 
    def test_test_user_request_without_client_id(self):
        result = requests.get('http://127.0.0.1:5000/maintenance_tracker/api/v1/getAllRequests/')
        self.assertEqual(result.json(),{"requests":"You have not created any requests yet"})
 
    
    
    

if __name__ == '__main__':
    unittest.main()