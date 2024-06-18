from utils.db import collection_tareas
from bson import ObjectId

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
    

    def get_user_tasks(self,username_id):
        try:
            user_tasks = collection_tareas.find({'usu_asignado': username_id})

            tasks_list = []
            for task in user_tasks:
                tasks_list.append({
                    '_id': str(task['_id']),
                    'titulo': task['titulo'],
                    'descripcion': task['descripcion'],
                    'fecha_hora_vencimiento': task['fecha_hora_vencimiento'],
                    'estado': task['estado'],
                    'tipo_tarea': task['tipo_tarea'],
                    'no_servicio': task['no_servicio']
                })

            return {'tasks': tasks_list}, 200
        except Exception as e:
            return {'error': str(e)}, 500


    def update_task_completion_date(self,task_id,current_date):
        try:
            result = collection_tareas.update_one(
                {'_id': ObjectId(task_id)},
                {'$set': {'estado': 'Completada', 'fecha_hora_completado': current_date}}
            )

            if result.modified_count > 0:
                return {'message': 'Tarea marcada como completada en la base de datos'}, 200
            else:
                return {'error': 'No se pudo actualizar la tarea'}, 404
        except Exception as e:
            return {'error': str(e)}, 500
        
    def get_task_recurrente(self):
        try:
            recurrent_tasks = collection_tareas.find({'recurrente': {'$exists': True, '$eq': True}})
            recurrent_tasks = list(recurrent_tasks)
            # print(recurrent_tasks)
            return {'tasks': recurrent_tasks}, 200
        except Exception as e:
            print(f"Error al obtener tareas recurrentes: {e}")
            return {'error': str(e)}, 500

tareas_repository = TareasRepository()