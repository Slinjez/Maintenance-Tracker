import sys
import unittest
import os
import json
#from flask import request
from app import routes 




class MaintenanceTrackerTest(unittest.TestCase):

    def setUp(self):
        self.routes = routes
        self.routes = routes.app.test_client()
        self.requestnoemail = {
        "useremail": "",
        "userpassword": "apassword"
        }    

    def test_user_signup(self):
        """
        Test if user is created successfully through the endpoint
        """                       
        result = routes.signup('/api/v1/users/',data=json.dumps(self.requestnoemail)
                                       ,content_type='application/json')
        self.assertEqual(result.json(),{"response": "email is required"})  

if __name__ == "__main__":
    unittest.main()          
