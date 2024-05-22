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