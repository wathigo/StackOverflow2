from . import ConfigTesting

import unittest
import json

class TestUsers(ConfigTesting, unittest.TestCase):
    def test_post(self):
        response = self.client.post('/api/v1/auth/signup',
                            data=json.dumps({
                            "email": "okwarjoseph",
                            "password": "jddbydjk"
                            }),
                            headers={"content-type": "application/json"})
        self.assertEqual(response.status_code, 400)
        response = self.client.post('/api/v1/auth/signup',
                            data=json.dumps({
                            "email": "okwarjoseph@gmail.com",
                            "password": "Okwar_2784"
                            }),
                            headers={"content-type": "application/json"})
        self.assertEqual(response.status_code, 201)
