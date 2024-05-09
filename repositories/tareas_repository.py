from utils.db import collection_tareas

class TareasRepository:

    def crearTarea(self,tarea_data):
        try:
            # Insertar los datos recibidos desde la aplicación frontend en la colección
            collection_tareas.insert_one(tarea_data)
            return {
                    'success': True, 
                    'message': 'Tarea creada exitosamente.'
                    }
        except Exception as e:
            return {
                    'success': False, 
                    'error': str(e)
                }
        
    
    def getTareas(self):
        try:
            data = list(collection_tareas.find({}, {'_id': 0}))
            return {
                'message': 'Tareas obtenidas exitosamente.',
                'success': True,
                'data': data
            }
        except Exception as e:
            return {
                'success': False,
                'error': str(e)
            }
    
tareas_repository = TareasRepository()