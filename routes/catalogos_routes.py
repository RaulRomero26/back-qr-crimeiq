from flask import Blueprint, request, jsonify
from usecase.catalogos_usecase import catalogos_usecase

catalogos_routes = Blueprint('catalogos_routes', __name__)

@catalogos_routes.route('/catalogo_usuarios', methods=['POST'])
def catalogo_usuarios():
    return catalogos_usecase.catalogo_usuarios()