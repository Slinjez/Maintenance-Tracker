'''the tests should cover 
1. when the request title is blank
2. when request description is blank
'''
import unittest

class TestCreateNewRequest(unittest.TestCase):

    def test_missing_request_title(self):
        result = createRequest("","request body","1","29 may 2018")
        self.assertEqual(result,'Please enter a title for your request')
    
    def test__missing_description(self):
        result = createRequest("request title","","1","29 may 2018")
        self.assertEqual(result,'Please enter a brief description for your request')


    
    

if __name__ == '__main__':
    unittest.main()
