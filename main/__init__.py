from flask import Flask
from main.api.users import users
ivan = Flask(__name__)
ivan.register_blueprint(users)