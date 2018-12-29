from flask_restful import Resource
from flask import jsonify, make_response, request

from ..models_users.models import UserRecords
from ...validators.validators import ValidateUser

class User(UserRecords, Resource):
    def __init__(self):
        self.records = UserRecords()
        self.valid  = ValidateUser()

    def post(self):
        data = request.get_json()
        if data['email'] is None or data['password'] is None:
            return make_response(jsonify({'error': 'Username and password required'}), 400)
        email = data['email']
        password = data['password']
        valid_email = self.valid.validate_email(email)
        if valid_email:
            return make_response(jsonify({"Invalid email": valid_email}), 400)

        valid_password = self.valid.validate_pasword(password)
        if valid_password:
            return make_response(jsonify({"Invalid password": valid_password}), 400)
        responce = self.records.save(email, password)
        return make_response(jsonify({"My new users are": responce}), 201)
