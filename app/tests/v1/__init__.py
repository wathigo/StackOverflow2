from app import create_app
from run import appl

from flask.testing import FlaskClient

class ConfigTesting():
     def setUp(self):
        appl.testing = True
        self.app = create_app()
        self.client = self.app.test_client()
