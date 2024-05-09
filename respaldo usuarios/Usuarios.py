from flask import Blueprint, send_from_directory, request, jsonify
from usecase.Usuario_usecase import login
from utils.db import db

Login = Blueprint('Login', __name__)

@Login.route('/login', methods=['POST'])
def Login_handler():
    return login()
