'''the tests should cover 
1. when user has no requests
2. test for request without user id
'''
import unittest
#from ../../app.py import app #failed

class TestGetAllUserRequests(unittest.TestCase):
    
    def test_client_with_no_request(self):
        result = getAllRequest(2)
        self.assertEqual(result,"You have not created any requests yet")
 
    def test_test_user_request_without_client_id(self):
        result = getAllRequest()
        self.assertEqual(result,"Cannot fetch results without user id")
    
    
    

if __name__ == '__main__':
    unittest.main()