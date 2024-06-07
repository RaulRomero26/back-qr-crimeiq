from flask import Blueprint, request, jsonify
from usecase.catalogos_usecase import catalogos_usecase

catalogos_routes = Blueprint('catalogos_routes', __name__)

@catalogos_routes.route('/catalogo_usuarios', methods=['POST'])
def catalogo_usuarios():
    return catalogos_usecase.catalogo_usuarios()

@catalogos_routes.route('/catalogo', methods=['GET'])
def get_catalogo():
    print('catalogo:', request.args.get('catalogo'))
    catalogo_buscado = request.args.get('catalogo')
    return catalogos_usecase.get_catalogo(catalogo_buscado)

@catalogos_routes.route('/catalogo', methods=['PUT'])
def update_catalogo():
    catalogo_data = request.json
    return catalogos_usecase.update_catalogo(catalogo_data)

@catalogos_routes.route('/catalogo', methods=['POST'])
def add_option_catalogo():
    catalogo_data = request.json
    print('catalogo_data:', catalogo_data)
    return catalogos_usecase.add_option(catalogo_data)

@catalogos_routes.route('/catalogo_activo', methods=['GET'])
def get_catalogo_activo():
    catalogo_buscado = request.args.get('catalogo')
    print('catalogo_buscado:', catalogo_buscado)
    return catalogos_usecase.get_catalogo_activo(catalogo_buscado)