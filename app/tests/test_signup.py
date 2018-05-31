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
    def test_unername_blank(self,requestnousername):
        result = requests.post('http://127.0.0.1:5000/api/v1/users/requests',data=json.dumps(requestnousername), content_type='application/json')
        assert result.status_code == 200
        self.assertEqual(result.json(), {"requests": "please enter a username"})
    def test_email_not_blank(self,requestnoemail):
        result = requests.post('http://127.0.0.1:5000/api/v1/users/requests',data=json.dumps(requestnoemail), content_type='application/json')
        assert result.status_code == 200
        self.assertEqual(result.json(), {"requests": "please enter an usermail"})
    
    def test_password1_not_blank(self,requestnops1):
        result = requests.post('http://127.0.0.1:5000/api/v1/users/requests',data=json.dumps(requestnops1), content_type='application/json')
        assert result.status_code == 200
        self.assertEqual(result.json(), {"requests": "please enter a password"})

    def test_password2_not_blank(self,requestnops2):
        result = requests.post('http://127.0.0.1:5000/api/v1/users/requests',data=json.dumps(requestnops2), content_type='application/json')
        assert result.status_code == 200
        self.assertEqual(result.json(), {"requests": "please confirm your password"})
    
    def test_passwords_match(self,requestmissmatchps):
        result = requests.post('http://127.0.0.1:5000/api/v1/users/requests',data=json.dumps(requestmissmatchps), content_type='application/json')
        assert result.status_code == 200
        self.assertEqual(result.json(), {"requests": "please enter matching passwords"})
    
    
if __name__ == '__main__':
    unittest.main()