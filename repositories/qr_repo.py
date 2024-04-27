from utils.db import db, collection

def insertar_res(data):
    try:
        # Insertar los datos recibidos desde la aplicación frontend en la colección
        result = collection.insert_one(data)
        print('ID del documento insertado:', result.inserted_id)
        return {'success': True, 'message': 'Datos guardados exitosamente.'}
    except Exception as e:
        print('Error al insertar datos en MongoDB:', str(e))
        return {'success': False, 'message': 'Error al guardar los datos en la base de datos.'}
