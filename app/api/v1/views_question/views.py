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

    def delete(self):
        res = self.records.empty_records()
        return make_response(jsonify({"My new records are": res}), 200)

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

    def delete(self, id):
        res = self.records.del_record(id)
        if res:
            return make_response(jsonify({"My new records are": res}), 200)
        else:
            return make_response(jsonify({"Msg": "Question record not found"}), 404)

    def put(self, id):
        data = request.get_json()
        category = data['category']
        question = data['question']
        res = self.records.replace(id, category, question)
        if res:
            return make_response(jsonify({"My updated records are": res}), 200)
        else:
            return make_response(jsonify({"Msg": "Question record not found"}), 404)
