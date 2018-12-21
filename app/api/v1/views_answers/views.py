from flask_restful import Resource
from flask import jsonify, make_response, request

from ..models_answers.models import AnswerRecord
class Answer(AnswerRecord, Resource):
    def __init__(self):
        self.records = AnswerRecord()

    def post(self, id):
        data = data = request.get_json()
        question_id = id
        answer = data['answer']
        responce = self.records.save(question_id, answer)
        return make_response(jsonify({"My new answer records are": responce}), 201)
