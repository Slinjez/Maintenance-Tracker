'''the tests should cover 
1. when user has no requests
'''
import unittest
import requests
import json
import sys
#from ../../app.py import app #failed


class TestGetAllUserRequests(unittest.TestCase):

    def test_client_with_no_request(self):
        result = requests.get('http://127.0.0.1:5000/api/v1/getAllRequests/3')
        self.assertEqual(
            result.json(), {"requests": "No requests for this user"})

    


if __name__ == '__main__':
    unittest.main()