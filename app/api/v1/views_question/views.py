from flask_restful import Resource
from flask import jsonify, make_response, request

from ..models_question.models import QuestionRecords

class Question(Resource, QuestionRecords):
    def __init__(self):
        self.records = QuestionRecords()

    def post(self):
         data = request.get_json()
         category = data['category']
         question = data['question']
         res = self.records.save(category, question)
         return make_response(jsonify({"My new records are": res}), 201)

    def get(self):
        res = self.records.get_records()
        return make_response(jsonify({"My new records are": res}), 200)

class QuestionId(Resource, QuestionRecords):
    def __init__(self):
        self.records = QuestionRecords()

    def get(self, id):
        rec = self.records.find(id)
        if rec:
            return make_response(jsonify({"My new records are": rec}), 200)
        else:
            return make_response(jsonify({"Msg": "Question record not found"}), 404)
