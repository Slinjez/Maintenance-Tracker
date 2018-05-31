'''the tests should cover 
1. username is not blank
2. email is not blank
3. passwords are not blank
4. passwords match
'''
import unittest
import requests
import json
import sys

class TestSignup(unittest.TestCase):
    requestalldata = {
        "username": "aname",
        "useremail": "somemail@mail",
        "userpassword1": "apassword",
        "userpassword2": "apassword"
    }
    requestnousername = {
        "username": "",
        "useremail": "nameless@mail",
        "userpassword1": "apassword",
        "userpassword2": "apassword"
    }
    requestnoemail = {
        "username": "no email guy",
        "useremail": "",
        "userpassword1": "apassword",
        "userpassword2": "apassword"
    }
    requestnops1 = {
        "username": "no password 1 guy",
        "useremail": "ihatepasswords@mail",
        "userpassword1": "",
        "userpassword2": "apassword"
    }
    requestnops2 = {
        "username": "no password 2 guy",
        "useremail": "ihatepasswords@mail",
        "userpassword1": "apassword",
        "userpassword2": ""
    }
    requestmissmatchps = {
        "username": "forgetful guy",
        "useremail": "forget@mail",
        "userpassword1": "apassword",
        "userpassword2": "forgot my password"
    }
    def test_unername_blank(self):
        headers = {'content-type': 'application/json'}
        result = requests.post('http://127.0.0.1:5000/api/v1/users/signup',data=json.dumps(self.requestnousername), headers=headers)
        #assert result.status_code == 200
        self.assertEqual(result.json(), {"response": "please enter a username"})
    def test_email_not_blank(self):
        headers = {'content-type': 'application/json'}
        result = requests.post('http://127.0.0.1:5000/api/v1/users/signup',data=json.dumps(self.requestnoemail), headers=headers)
        #assert result.status_code == 200
        self.assertEqual(result.json(), {"response": "please enter an usermail"})
    
    def test_password1_not_blank(self):
        headers = {'content-type': 'application/json'}
        result = requests.post('http://127.0.0.1:5000/api/v1/users/signup',data=json.dumps(self.requestnops1), headers=headers)
        #assert result.status_code == 200
        self.assertEqual(result.json(), {"response": "please enter a password"})

    def test_password2_not_blank(self):
        headers = {'content-type': 'application/json'}
        result = requests.post('http://127.0.0.1:5000/api/v1/users/signup',data=json.dumps(self.requestnops2), headers=headers)
        assert result.status_code == 200
        self.assertEqual(result.json(), {"response": "please confirm your password"})
    
    def test_passwords_match(self):
        headers = {'content-type': 'application/json'}
        result = requests.post('http://127.0.0.1:5000/api/v1/users/signup',data=json.dumps(self.requestmissmatchps), headers=headers)
        assert result.status_code == 200
        self.assertEqual(result.json(), {"response": "please enter matching passwords"})
    
    
if __name__ == '__main__':
    unittest.main()