from flask import Blueprint,Flask
from . import users 
ivan = Flask(__name__)
users = Blueprint('users',__name__)

