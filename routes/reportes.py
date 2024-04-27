from flask import Blueprint, request, jsonify
from utils.db import db_Inc, collection_Inc

reportes = Blueprint('reportes', __name__)

@reportes.route('/guardar_reporte', methods=['POST'])
def guardar_reporte():
    try:
        data = request.json
        
        # Validación de datos
        if not all(key in data for key in ('fechaHora', 'latitud', 'longitud', 'descripcion', 'nivelGravedad', 'tipoIncidente')):
            return jsonify({'error': 'Faltan campos obligatorios en los datos recibidos'}), 400
        
        # Insertar datos en la colección de incidencias
        collection_Inc.insert_one(data)
        
        return jsonify({'message': 'Datos del reporte guardados exitosamente'}), 200
    
    except KeyError as e:
        return jsonify({'error': 'Falta el campo obligatorio: {}'.format(str(e))}), 400
    
    except Exception as e:
        return jsonify({'error': 'Error al guardar el reporte: {}'.format(str(e))}), 500

