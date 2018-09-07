from flask import Blueprint,Flask
from . import users 
ivan = Flask(__name__)
ivan.register_blueprint(users)

