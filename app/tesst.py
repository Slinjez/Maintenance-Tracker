from app import app
import unittest
import json


class MaintenanceTrackerApiTest(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.request = {

            'requestid': 1,
            'requestorid': 1,
            'requesttitle': 'An Awesome Title',
            'requestdescription': 'This is my request description',
            "requesttype": 1,
            'requestcreationdate': '30 may 2018',
            'requeststatus': 1

        }

    def test_create_request(self):
        """
        Test that a user can create a request
        """
        resource = self.app.post('/users/requests/', data=self.request)
        self.assertEqual(resource.status_code, 201)
        self.assertIn(self.request, str(resource.data))
