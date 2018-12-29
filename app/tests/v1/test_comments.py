from . import ConfigTesting

import unittest
import json

class TestComments(ConfigTesting, unittest.TestCase):
    def create_record(self):
        new_rec = {
        "comment": "This helped me alot"
        }
        response = self.client.post('/api/v1/questions/answer/1/comments',
                            data=json.dumps(new_rec),
                            headers={"content-type": "application/json"})
        return response

    def test_01_post(self):
        r = self.create_record()
        self.assertEqual(r.status_code, 201)

    def test_02_(self):
        self.create_record()
        r = self.client.get("/api/v1/questions/answer/1/comments", headers={"content-type": "application/json"})
        self.assertEqual(r.status_code, 200)
