'''the tests should cover 
1. email is not blank
2. password is not blank
4. password is correct
5. the provided email is registered or existing
'''
import unittest

class TestLogIn(unittest.TestCase):
    
    def test_email_not_blank(self):
        result = logIn("","ps")
        self.assertEqual(result,'Please enter your email address')
    
    def test_password_not_blank(self):
        result = logIn("email@emal","")
        self.assertEqual(result,'Please enter your password')    
    
    def test_test_email_is_existing(self):
        result = logIn("email@emal","ps")
        self.assertEqual(result,'You have not registered. Please sign up')
    
    def test_password_is_correct(self):
        result = logIn("email@emal","ps")
        self.assertEqual(result,'You have entered incorrect login details')
    

if __name__ == '__main__':
    unittest.main()