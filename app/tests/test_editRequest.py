# '''the tests should cover 
# 1. test non existing request
# '''
# import unittest
# import requests
# import json
# import sys
# import pdb
# class TestEditRequest(unittest.TestCase):
#     testnotexisting = {
#          "requestid": "8"
#     }
    
#     def test_unexisting_requestId(self):
#         headers = {'content-type': 'application/json'}

#         result = requests.put('http://127.0.0.1:5000/api/v1/users/requests/',data=json.dumps(self.testnotexisting), headers=headers)
#         #pdb.set_trace()
#         self.assertEqual(
#             result.json(), {"response": "Cannot edit this request"})
    

# if __name__ == '__main__':
#     unittest.main()