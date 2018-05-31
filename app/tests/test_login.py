'''the tests should cover 
1. email is not blank
2. password is not blank
4. password is correct
5. the provided email is registered or existing
'''
import unittest
import requests
import json
import sys


class TestLogIn(unittest.TestCase):
    requestalldata = {
        "useremail": "somemail@mail",
        "userpassword": "apassword"
    }
    requestnoemail = {
        "useremail": "",
        "userpassword": "apassword"
    }
    requestnopassword = {
        "useremail": "nops@mail",
        "userpassword": ""
    }
    requestnotexisting = {
        "useremail": "nops@mail",
        "userpassword": "somps"
    }
    requestbadpassword = {
        "useremail": "mwangiwathiga@gmail.com",
        "userpassword": "mypss"
    }

    def test_email_not_blank(self):
        headers = {'content-type': 'application/json'}
        result = requests.post('http://127.0.0.1:5000/api/v1/users/login',
                               data=json.dumps(self.requestnoemail), headers=headers)
        #assert result.status_code == 200
        self.assertEqual(result.json(), {"response": "email is required"})

    def test_password_not_blank(self):
        headers = {'content-type': 'application/json'}
        result = requests.post('http://127.0.0.1:5000/api/v1/users/login',
                               data=json.dumps(self.requestnopassword), headers=headers)
        #assert result.status_code == 200
        self.assertEqual(result.json(), {"response": "password is required"})

    def test_test_email_is_existing(self):
        headers = {'content-type': 'application/json'}
        result = requests.post('http://127.0.0.1:5000/api/v1/users/login',
                               data=json.dumps(self.requestnotexisting), headers=headers)
        #assert result.status_code == 200
        self.assertEqual(
            result.json(), {"response": "Unregistered email"})

    def test_password_is_correct(self):
        headers = {'content-type': 'application/json'}
        result = requests.post('http://127.0.0.1:5000/api/v1/users/login',
                               data=json.dumps(self.requestbadpassword), headers=headers)
        #assert result.status_code == 200
        self.assertEqual(result.json(), {"response": "Invalid credentials"})


if __name__ == '__main__':
    unittest.main()
