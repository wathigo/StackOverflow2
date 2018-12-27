from flask_restful import Resource
from flask import jsonify, make_response, request

from ..models_answers.models import AnswerRecord
class Answer(AnswerRecord, Resource):
    def __init__(self):
        self.records = AnswerRecord()

    def post(self, id):
        data = request.get_json()
        question_id = id
        answer = data['answer']
        responce = self.records.save(question_id, answer)
        return make_response(jsonify({"My new answer records are": responce}), 201)

class AnswerId(AnswerRecord, Resource):
    def __init__(self):
        self.records = AnswerRecord()

    def get(self, id):
        responce = self.records.get_answer(id)
        if responce:
            return make_response(jsonify({"The answer to the quesion is": responce}), 200)
        else:
            return make_response(jsonify({"Msg": "item not found"}), 404)

    def put(self, id):
        responce = self.records.mark_accepted(id)
        if responce:
            return make_response(jsonify({"My updated answer records are": responce}), 201)
        else:
            return make_response(jsonify({"Msg": "item not found"}), 404)

class AnswerQuestion(AnswerRecord, Resource):
    def  __init__(self):
        self.records = AnswerRecord()

    def put(self, answer_id):
        data = request.get_json()
        answer = data['answer']
        responce = self.records.replace(answer_id, answer)
        return make_response(jsonify({"My new answer records are": responce}), 201)
