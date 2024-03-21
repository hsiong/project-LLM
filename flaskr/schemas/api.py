

from flask import Blueprint

home_api = Blueprint('api', __name__)

@home_api.route('/welcome')
def welcome():
    return "你好"