from flask_restful import Api, Resource
from flask import Blueprint

version_one = Blueprint('api_v1', __name__, url_prefix='/api/v1')
api = Api(version_one)

from .views_question.views import Question, QuestionId
api.add_resource(Question, '/questions')
api.add_resource(QuestionId, '/questions/<int:id>')
