'''the tests should cover 
1. when the request title is blank
2. when request description is blank
'''
import unittest
import requests
import json
import sys
import pdb
# pdb.set_trace()


class TestCreateNewRequest(unittest.TestCase):
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

        result = requests.post('http://127.0.0.1:5000/api/v1/users/requests',
                               data=json.dumps(self.testvariableNoTitle), headers=headers)
        # pdb.set_trace()
        self.assertEqual(
            result.json(), {"response": "Enter request title"})
    def test_missing_request_description(self):
        headers = {'content-type': 'application/json'}

        result = requests.post('http://127.0.0.1:5000/api/v1/users/requests',
                               data=json.dumps(self.testvariableNoDescription), headers=headers)
        # pdb.set_trace()
        self.assertEqual(
            result.json(), {"response": "Enter request description"})

    def test_missing_request_type(self):
        headers = {'content-type': 'application/json'}

        result = requests.post('http://127.0.0.1:5000/api/v1/users/requests',
                               data=json.dumps(self.testvariableNoType), headers=headers)
        # pdb.set_trace()
        self.assertEqual(
            result.json(), {"response": "Select request type"})


if __name__ == '__main__':
    unittest.main()
