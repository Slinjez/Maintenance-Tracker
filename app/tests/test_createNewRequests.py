'''the tests should cover 
1. when the request title is blank
2. when request description is blank
'''
import unittest
import requests
import json
import sys


class TestCreateNewRequest(unittest.TestCase):
    request = {
        "requestid": 8,
        "requestorid": 3,
        "requesttitle": "Just Another Awesome Title",
        "requestdescription": "This is not my request description",
        "requestcreationdate": "31 may 2018",
        "requeststatus": 1
    }
    #requestJson=jsonify({"therq":request})

    def test_missing_request_title(self,request):
        result = requests.post('http://127.0.0.1:5000//api/v1/users/requests',data=json.dumps(request), content_type='application/json')
        self.assertEqual(result.json(), {"requests": "Please enter request title"})


if __name__ == '__main__':
    unittest.main()
