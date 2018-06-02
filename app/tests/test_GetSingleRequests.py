# '''the tests should cover 
# 1. when the request is missing
# '''
# from app import app
# import unittest
# from flask import request
# import json
# import sys

# class TestGetSingleUserRequest(unittest.TestCase):
#     requestmissing={"requestid"=""}

#     def setup(self):
#         app=flask.Flask(__name__)
     
    
    
#     def test_missing_request(self):
#         headers = {'content-type': 'application/json'}
#         with app.test_client() as c:
#             result =c.post('/api/v1/users/requests/',data=json.dumps(self.requestmissing),headers=headers)
#             self.assertEqual(result.status_code,404)
        
    
    
    
    

# if __name__ == '__main__':
#     unittest.main()