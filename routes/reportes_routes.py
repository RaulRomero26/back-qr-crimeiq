from flask import Blueprint, request
from usecase.reportes_usecase import reportes_usecase

reportes_routes = Blueprint('reportes_routes', __name__)

@reportes_routes.route('/guardar_reporte', methods=['POST'])
def guardar_reporte():
    reporte_data = request.get_json()
    return reportes_usecase.guardar_reporte(reporte_data)

@reportes_routes.route('/alerta_emergencia', methods=['POST'])
def guardar_alerta_emergencia():
    alerta_data = request.get_json()
    return reportes_usecase.guardar_alerta(alerta_data)