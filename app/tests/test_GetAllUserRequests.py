'''the tests should cover 
1. when user has no requests
'''
from app import app
import unittest
from flask import request
import json
import sys
#from ../../app.py import app #failed


class TestGetAllUserRequests(unittest.TestCase):
    def setup(self):
        app=flask.Flask(__name__)

    requestnotexisting=8
    requestinvalid="R" 
    requestempty=None
    requestgood=2

    def test_client_with_no_request(self):                
        headers = {'content-type': 'application/json'}
        with app.test_client() as c:
            result =c.get('/api/v1/users/requests/',data=json.dumps(self.requestnotexisting),headers=headers)
            self.assertEqual(result.status_code,404)
    
    def test_empty_id(self):
        headers = {'content-type': 'application/json'}
        with app.test_client() as c:
            result =c.get('api/v1/users/requests/',data=self.requestempty,headers=headers)
            self.assertEqual(result.status_code,404)

    def test_good_id(self):
        headers = {'content-type': 'application/json'}
        with app.test_client() as c:
            result =c.get('api/v1/users/requests/',data=self.requestempty,headers=headers)
            self.assertEqual(result.status_code,404)
    
    

    


if __name__ == '__main__':
    unittest.main()