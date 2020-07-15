from flask import Flask
from flask_jwt_extended import JWTManager
from flask_restful import Api

from app import config
from app.database.mongo_service import mongo_global_init
from app.views import api_activate_resources

print("Initialising the server...")

current_config = config.BaseConfig()

app = Flask(__name__)
api = Api(app)
jwt = JWTManager(app)

current_config.set_app(app)

db = mongo_global_init(config=current_config)

api_activate_resources(api)