from flask_restful import Resource
from flask import jsonify, make_response, request

from ..models_comments.models import CommentRecord

class Comment(CommentRecord, Resource):
    def __init__(self):
        self.comm_rec = CommentRecord()

    def post(self, answer_id):
        data = request.get_json()
        comment = data['comment']
        responce = self.comm_rec.save(answer_id, comment)
        return make_response(jsonify({"My new comment records are": responce}), 201)

    def get(self, answer_id):
        responce = self.comm_rec.get_item(answer_id)
        if responce:
            return make_response(jsonify({"The comment(s) to the answer is": responce}), 200)

        else:
            return make_response(jsonify({"Msg": "item not found"}), 404)
