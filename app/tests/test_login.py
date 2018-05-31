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
        "userpassword": "myps"
    }

    def test_email_not_blank(self, requestnoemail):
        result = requests.post('http://127.0.0.1:5000/api/v1/users/login',
                               data=json.dumps(requestnoemail), content_type='application/json')
        assert result.status_code == 200
        self.assertEqual(result.json(), {"response": "email is required"})

    def test_password_not_blank(self, requestnopassword):
        result = requests.post('http://127.0.0.1:5000/api/v1/users/login',
                               data=json.dumps(requestnopassword), content_type='application/json')
        assert result.status_code == 200
        self.assertEqual(result.json(), {"response": "password is required"})

    def test_test_email_is_existing(self, requestnotexisting):
        result = requests.post('http://127.0.0.1:5000/api/v1/users/login',
                               data=json.dumps(requestnotexisting), content_type='application/json')
        assert result.status_code == 200
        self.assertEqual(
            result.json(), {"response": "email is not registered"})

    def test_password_is_correct(self, requestbadpassword):
        result = requests.post('http://127.0.0.1:5000/api/v1/users/login',
                               data=json.dumps(requestbadpassword), content_type='application/json')
        assert result.status_code == 200
        self.assertEqual(result.json(), {"response": "Invalid credentials"})


if __name__ == '__main__':
    unittest.main()
