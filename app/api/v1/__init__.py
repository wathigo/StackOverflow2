from flask_restful import Api, Resource
from flask import Blueprint

version_one = Blueprint('api_v1', __name__, url_prefix='/api/v1')
api = Api(version_one)

from .views_question.views import Question, QuestionId
from .views_answers.views import Answer, AnswerId
api.add_resource(Question, '/questions')
api.add_resource(QuestionId, '/questions/<int:id>')
api.add_resource(Answer, '/questions/<int:id>/answers')
api.add_resource(AnswerId, '/questions/answers/<int:id>')
