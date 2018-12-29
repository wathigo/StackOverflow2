from . import ConfigTesting

import unittest
import json

class TestAnswers(ConfigTesting, unittest.TestCase):
    def create_record(self):
        new_rec = {
        "answer": "We have while loops in python"
        }
        response = self.client.post('/api/v1/questions/4/answers',
                            data=json.dumps(new_rec),
                            headers={"content-type": "application/json"})
        return response

    def test_01_post(self):
        r = self.create_record()
        self.assertEqual(r.status_code, 201)

    def test_02_get(self):
        self.create_record()
        r = self.client.get("/api/v1/questions/answers/1", headers={"content-type": "application/json"})
        self.assertEqual(r.status_code, 200)

    def test_03_put(self):
        self.create_record()
        r = self.client.put("/api/v1/questions/answers/1", headers={"content-type": "application/json"})
        self.assertEqual(r.status_code, 201)
        r = self.client.put("/api/v1/questions/answer/1", data = json.dumps({
                "answer": "We have while loops in python. In additional to while loops, for loops are also common in python"
                }), headers={"content-type": "application/json"})
        self.assertEqual(r.status_code, 201)
