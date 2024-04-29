from flask import Blueprint, send_from_directory, request, jsonify
from usecase.qr_usecase import generar_qr, captura_qr
from utils.db import db
import os

qr = Blueprint('qr', __name__)

@qr.route('/generar_qr', methods=['POST'])
def generar_qr_handler():
    return generar_qr()

@qr.route('/imagenes/<path:filename>')
def servir_imagen_handler(filename):
    directorio = os.path.join(os.getcwd(), 'RESULTADO_QR')
    return send_from_directory(directorio, filename)

@qr.route('/guardar_datos', methods=['POST'])
def capturar_qr_handler():
    data = request.json  # Obtener los datos del cuerpo de la solicitud
    success = captura_qr(data)  # Llamar a la función que captura el QR
    
    if success:
        return jsonify({'success': True, 'message': 'Datos guardados exitosamente'}), 200
    else:
        return jsonify({'success': False, 'message': 'Error al guardar los datos'}), 500

@qr.route('/api/recorridos')
def obtener_recorridos():
    collection = db.get_collection('RECORRIDOS')  # Obtener la colección de recorridos
    datos = list(collection.find({}, {'_id': 0}))  # Obtener todos los documentos de la colección
    return jsonify(datos)