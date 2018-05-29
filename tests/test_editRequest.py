'''the tests should cover 
1. test non existing request
2. test request with wrong request id format
'''
import unittest

class TestEditRequest(unittest.TestCase):
    
    def test_unexisting_requestId(self):
        result = editRequest(3):
        self.assertEqual(result,"this request may have been deleted")
        
    def test_request_wrong_id_format(self):
        result = editRequest('three')
        self.assertEqual(result,"This request id is invalid")
    
    

if __name__ == '__main__':
    unittest.main()
