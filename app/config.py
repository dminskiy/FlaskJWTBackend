import os

mongoDB_local_base = 'mongodb://localhost:27017/'

class BaseConfig:
    def __init__(self):
        self.DEBUG = False
        self.PROPAGATE_EXCPTNS = True
        self.ENV = 'production'
        self.MONGODB_URI = mongoDB_local_base
        self.MONGODB_ALIAS = "default"
        self.MONGODB_NAME = "openWeatherApiTest"
        self.JWT_SECRET_KEY = "jwt_key"

    def set_app(self, app):
        app.config['JWT_SECRET_KEY'] = self.JWT_SECRET_KEY
        app.config['PROPAGATE_EXCEPTIONS'] = self.PROPAGATE_EXCPTNS
        app.config['DEBUG'] = self.DEBUG
        app.config['ENV'] = self.ENV