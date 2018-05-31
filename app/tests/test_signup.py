'''the tests should cover 
1. username is not blank
2. email is not blank
3. passwords are not blank
4. passwords match
5. the provided email is not already registered
'''
import unittest

class TestSignup(unittest.TestCase):
    def test_unername_blank(self):
        result = signUp("","email@email","ps1","ps2")
        self.assertEqual(result,'Please enter your preffered username')
    def test_email_not_blank(self):
        result = signUp("thename","","ps1","ps2")
        self.assertEqual(result,'Please enter your email address')
    
    def test_password1_not_blank(self):
        result = signUp("thename","email@email","","ps2")
        self.assertEqual(result,'Please enter a password of choice')

    def test_password2_not_blank(self):
        result = signUp("thename","email@email","ps1","")
        self.assertEqual(result,'Please confirm your password')
    
    def test_passwords_match(self):
        result = signUp("thename","email@email","ps1","ps2")
        self.assertEqual(result,'Your passwords mismatch, please try again')
    
    def test_user_email_isnot_registered(self):
        result = signUpAction("thename","email@email","ps1","ps2")
        self.assertEqual(result,'You have already registered with us. Please log in.')

if __name__ == '__main__':
    unittest.main()