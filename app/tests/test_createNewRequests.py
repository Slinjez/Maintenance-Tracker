'''the tests should cover 
1. when the request title is blank
2. when request description is blank
'''
from app import app
import unittest
from flask import request
import json
import sys


# pdb.set_trace()


class TestCreateNewRequest(unittest.TestCase):
    def setup(self):
        app = flask.Flask(__name__)

    testvariable = {
        "requesttitle": "Just Another Awesome Title",
        "requestdescription": "This is not my request description",
        "requesttype": 1
    }
    testvariableNoTitle = {
        "requesttitle": "",
        "requestdescription": "This is not my request description",
        "requesttype": 1
    }
    testvariableNoDescription = {
        "requesttitle": "The title",
        "requestdescription": "",
        "requesttype": 1
    }
    testvariableNoType = {
        "requesttitle": "The title",
        "requesttype": None,#bet will never find out
        "requestdescription": "The description"
        
    }
    # requestJson=jsonify({"therq":request})

    def test_missing_request_title(self):        
        headers = {'content-type': 'application/json'}
        with app.test_client() as c:
            result = c.post('/api/v1/users/requests',
                           data=json.dumps(self.testvariableNoTitle), headers=headers)
            self.assertEqual(result.status_code, 206)

    def test_missing_request_description(self):
        headers = {'content-type': 'application/json'} 
        with app.test_client() as c:
            result = c.post('/api/v1/users/requests',
                           data=json.dumps(self.testvariableNoDescription), headers=headers)
            self.assertEqual(result.status_code, 206)

    def test_missing_request_type(self):
        headers = {'content-type': 'application/json'}
        with app.test_client() as c:
            result = c.post('/api/v1/users/requests',
                           data=json.dumps(self.testvariableNoType), headers=headers)
            self.assertEqual(result.status_code, 206)
    
    def test_good_entry(self):
        headers = {'content-type': 'application/json'}
        with app.test_client() as c:
            result = c.post('/api/v1/users/requests',
                           data=json.dumps(self.testvariable), headers=headers)
            self.assertEqual(result.status_code, 200)
        
        


if __name__ == '__main__':
    unittest.main()
