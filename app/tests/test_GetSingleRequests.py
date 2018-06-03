'''the tests should cover 
1. when the request is missing
'''
from app import app
import unittest
from flask import request
import json
import sys

class TestGetSingleUserRequest(unittest.TestCase):
    def setup(self):
        app=flask.Flask(__name__)

    requestnotexisting=8
    requestinvalid="R" 
    requestempty=None
    requestgoodid="2"

    
    def test_missing_request(self):
        headers = {'content-type': 'application/json'}
        with app.test_client() as c:
            result =c.get('/api/v1/users/requests/8',headers=headers)
            self.assertEqual(result.status_code,404)
    
    def test_invalid_id(self):
        headers = {'content-type': 'application/json'}
        with app.test_client() as c:
            result =c.get('/api/v1/users/requests/R',headers=headers)
            self.assertEqual(result.status_code,405)

    def test_empty_id(self):
        headers = {'content-type': 'application/json'}
        with app.test_client() as c:
            result =c.get('/api/v1/users/requests/',data=self.requestempty,headers=headers)
            self.assertEqual(result.status_code,404)
    
    def test_good_id(self):
        headers = {'content-type': 'application/json'}
        with app.test_client() as c:
            result =c.get('/api/v1/users/requests/',data=self.requestgoodid,headers=headers)
            self.assertEqual(result.status_code,404)
    
    
    
    

if __name__ == '__main__':
    unittest.main()