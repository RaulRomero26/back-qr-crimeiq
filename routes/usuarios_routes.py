from flask import Blueprint, request
from usecase import usuarios_usecase

usuarios_routes = Blueprint('usuarios_routes', __name__)

@usuarios_routes.route('/registrar', methods=['POST'])
def registrar_usuario():
    usuario_data = request.get_json()
    return usuarios_usecase.registrar_usuario(usuario_data)

@usuarios_routes.route('/all-usuarios')
def get_usuarios():
    return usuarios_usecase.get_usuarios()