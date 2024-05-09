from flask import Blueprint, request
from usecase.auth_usecase import auth_usecase

auth_routes = Blueprint('auth_routes', __name__)

@auth_routes.route('/login', methods=['POST'])
def login():
    login_data = request.get_json()
    return auth_usecase.login(login_data)