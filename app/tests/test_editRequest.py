'''the tests should cover 
1. test non existing request
'''
from app import app
import unittest
from flask import request
import json
import sys


class TestEditRequest(unittest.TestCase):
    def setup(self):
        app = flask.Flask(__name__)

    testnotexisting = {
        "requestid": "8"

    }
    badrequestid = {
        "badrequestid": "8"
    }
    wrongdtyperequestid = {
        "badrequestid": "R"
    }

    def test_unexisting_requestId(self):
        headers = {'content-type': 'application/json'}
        with app.test_client() as c:
            result = c.put('/api/v1/users/requests/',
                           data=json.dumps(self.testnotexisting), headers=headers)
            self.assertEqual(result.status_code, 404)

    def test_bad_requestId(self):
        headers = {'content-type': 'application/json'}
        with app.test_client() as c:
            result = c.put('/api/v1/users/requests/',
                           data=json.dumps(self.badrequestid), headers=headers)
            self.assertEqual(result.status_code, 404)

    def test_invalid_requestId(self):
        headers = {'content-type': 'application/json'}
        with app.test_client() as c:
            result = c.put('/api/v1/users/requests/',
                           data=json.dumps(self.wrongdtyperequestid), headers=headers)
            self.assertEqual(result.status_code, 404)


if __name__ == '__main__':
    unittest.main()
