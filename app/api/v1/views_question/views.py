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
