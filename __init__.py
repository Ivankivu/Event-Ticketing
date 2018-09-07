from flask import Blueprint,Flask
from . import users,api
ivan = Flask(__name__)
man = Flask(__name__)
ivan.register_blueprint(users)
man.register_blueprint(api)

