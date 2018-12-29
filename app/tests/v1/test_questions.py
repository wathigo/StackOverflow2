from . import ConfigTesting

import unittest
import json

class TestQuestionEndpoints(ConfigTesting, unittest.TestCase):
     def create_record(self):
        new_rec = {
        "category": "PROGRAMMING",
        "question": "How many loops do we have in programming"
        }
        response = self.client.post('/api/v1/questions',
                            data=json.dumps(new_rec),
                            headers={"content-type": "application/json"})
        return response

     def test_01_post(self):
         r = self.create_record()
         self.assertEqual(r.status_code, 201)

     def test_02_get(self):
         self.create_record()
         r = self.client.get("/api/v1/questions", headers={"content-type": "application/json"})
         self.assertEqual(r.status_code, 200)
         r = self.client.get("/api/v1/questions/1", headers={"content-type": "application/json"})
         self.assertEqual(r.status_code, 200)

     def test_03_delete(self):
         self.create_record()
         r = self.client.delete("/api/v1/questions")
         self.assertEqual(r.status_code, 200)
         r = self.client.delete("/api/v1/questions/1")
         self.assertEqual(r.status_code, 404)

     def test_04_put(self):
         self.create_record()
         r = self.client.put("/api/v1/questions/1", data = json.dumps({
                 "category": "PYTHON",
                 "question": "What types loops do we have in python"
                 }), headers={"content-type": "application/json"})
         self.assertEqual(r.status_code, 200)
