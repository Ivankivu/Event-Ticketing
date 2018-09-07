from flask import Blueprint,Flask
from . import api 
man = Flask(__name__)
people = Blueprint('api',__name__)

