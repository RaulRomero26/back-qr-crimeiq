from utils.db import collection_tareas

def crearTarea(data):
    try:
        # Insertar los datos recibidos desde la aplicación frontend en la colección
        result = collection_tareas.insert_one(data)
        print(result)
        print('ID del documento insertado:', result.inserted_id)
        return {'success': True, 'message': 'Tarea creada exitosamente.'}
    except Exception as e:
        print('Error al insertar datos en MongoDB:', str(e))
        return {'success': False, 'message': 'Error al guardar los datos en la base de datos.'}
