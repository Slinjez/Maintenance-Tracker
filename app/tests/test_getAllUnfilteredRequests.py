'''the tests should cover 
1. when no requests are available
'''
import unittest
import requests
import json
import sys
#from ../../app.py import app #failed


class TestGetAllUserRequests(unittest.TestCase):

    def test_client_with_no_request(self):
        result = requests.get('http://127.0.0.1:5000/api/v1/requests')
        self.assertEqual(
            result.json(), {"requests": "No requests os for now"})

    


if __name__ == '__main__':
    unittest.main()