from utils.db import db, collection, collection_qr

def insertar_res(data):
    try:
        # Insertar los datos recibidos desde la aplicación frontend en la colección
        result = collection.insert_one(data)
        print('ID del documento insertado:', result.inserted_id)
        return {'success': True, 'message': 'Datos guardados exitosamente.'}
    except Exception as e:
        print('Error al insertar datos en MongoDB:', str(e))
        return {'success': False, 'message': 'Error al guardar los datos en la base de datos.'}

def obtener_qrs_repo():
    try:
        # Obtener todos los documentos de la colección de códigos QR generados
        datos = list(collection_qr.find({}, {'_id': 0}))
        return {'success': True, 'data': datos}
    except Exception as e:
        print('Error al obtener los datos de la base de datos:', str(e))
        return {'success': False, 'message': 'Error al obtener los datos de la base de datos.'}
