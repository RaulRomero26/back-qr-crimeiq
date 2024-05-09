from flask import Blueprint, send_from_directory, request, jsonify
from usecase.qr_usecase import qr_usecase
import os

qr_routes = Blueprint('qr_routes', __name__)

#Obtener todos los QR
@qr_routes.route('/all-qr')
def obtener_qrs():
    return qr_usecase.obtener_qrs()

#Gnerar un QR con los datos proporcionados
@qr_routes.route('/generar_qr', methods=['POST'])
def generar_qr():
    qr_data = request.get_json()
    return qr_usecase.generar_qr(qr_data)

#Capturar cuando se escanea un QR
@qr_routes.route('/guardar_datos', methods=['POST'])
def capturar_qr():
    qr_data = request.get_json()  # Obtener los datos del cuerpo de la solicitud
    return qr_usecase.capturar_qr(qr_data)

#Obtener todos los escaneos de QR/ recorridos
@qr_routes.route('/recorridos')
def obtener_recorridos():
    return qr_usecase.obtener_recorridos()

#Servir imagen de un QR
@qr_routes.route('/imagenes/<path:filename>')
def servir_imagen_handler(filename):
    directorio = os.path.join(os.getcwd(), 'RESULTADO_QR')
    return send_from_directory(directorio, filename)