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


def getTareas():
    try:
        # Obtener todas las tareas de la colección
        tareas = collection_tareas.find()
        tareas_list = []
        for tarea in tareas:
            tarea['_id'] = str(tarea['_id'])
            tareas_list.append(tarea)
        return {'success': True, 'data': tareas_list}
    except Exception as e:
        print('Error al obtener datos de MongoDB:', str(e))
        return {'success': False, 'message': 'Error al obtener los datos de la base de datos.'}