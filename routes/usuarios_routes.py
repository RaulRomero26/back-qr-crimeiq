from flask import Blueprint, request, send_from_directory
from usecase.usuarios_usecase import usuarios_usecase
import os


usuarios_routes = Blueprint('usuarios_routes', __name__)

@usuarios_routes.route('/registrar', methods=['POST'])
def registrar_usuario():
    usuario_data = request.form.to_dict()
    archivos_data = request.files
    print(request.files)
    print(usuario_data)
    return usuarios_usecase.registrar_usuario(usuario_data,archivos_data)

@usuarios_routes.route('/all-usuarios')
def get_usuarios():
    return usuarios_usecase.get_usuarios()

@usuarios_routes.route('/imagenes/usuarios/<path:filename>')
def servir_imagen_handler(filename):
    directorio = os.path.join(os.getcwd(), 'USUARIOS')
    return send_from_directory(directorio, filename)

@usuarios_routes.route('/usuarios-asignados', methods=['GET'])
def get_usuarios_asignados():
    serv_asginado = request.args.get('serv_asignado')
    if not serv_asginado:
        return {
            'success': False,
            'message': 'El parámetro Serv_asignado es requerido.'
        }, 400
    
    return usuarios_usecase.get_usuarios_asignados(serv_asginado)

@usuarios_routes.route('actualizar-usuario', methods=['POST'])
def actualizar_usuario():
    usuario_data = request.form.to_dict()
    archivos_data = request.files
    print(request.files)
    print(usuario_data)
    return usuarios_usecase.actualizar_usuario(usuario_data,archivos_data)