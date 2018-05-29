'''the tests should cover 
1. when the request is missing
1. when request id is invalid
'''
import unittest

class TestGetSingleUserRequest(unittest.TestCase):
    
    def test_missing_request(self):
        result = getSingleRequest(2)
        self.assertEqual(result,'This request may  have been deleted')
    
    def test_invalid_id_format(self):
        result = getSingleRequest(two)
        self.assertEqual(result,'This is an invalid request id. Use numbers')
    
    

if __name__ == '__main__':
    unittest.main()