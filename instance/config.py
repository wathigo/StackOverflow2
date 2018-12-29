
import os


class Config(object):
    """
        Parent configuration class.
    """
    DEBUG = False


class TestingConfig(Config):
    """
        Configurations for Testing
    """
    TESTING = True
    DEBUG = True
    os.environ['ENV'] = 'testing'
