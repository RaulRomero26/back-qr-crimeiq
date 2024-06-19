from utils.db import collection_tareas
from bson import ObjectId
from datetime import datetime

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
            # Obtener el día de la semana actual
            current_day_english = datetime.now().strftime('%A').lower()
            # Mapear los días de la semana en inglés a español
            days_of_week = {
                'monday': 'Lunes',
                'tuesday': 'Martes',
                'wednesday': 'Miércoles',
                'thursday': 'Jueves',
                'friday': 'Viernes',
                'saturday': 'Sábado',
                'sunday': 'Domingo'
            }

            # Obtener el día de la semana actual en español
            current_day_spanish = days_of_week.get(current_day_english)
            print(current_day_spanish)
            recurrent_tasks = collection_tareas.find({'recurrente': {'$exists': True, '$eq': True}})
            recurrent_tasks = list(recurrent_tasks)
            # print(recurrent_tasks)

             # Crear nuevas tareas a partir de las tareas recurrentes
            new_tasks = []
            for task in recurrent_tasks:
                if task['dias_semana'].get(current_day_spanish, False):
                    new_task = task.copy()
                    new_task.pop('dias_semana', None)
                    new_task.pop('recurrente', None)
                    new_tasks.append(new_task)
                    print('hay nueva')
                    print(new_task)
                    
            return {'tasks': recurrent_tasks}, 200
        except Exception as e:
            print(f"Error al obtener tareas recurrentes: {e}")
            return {'error': str(e)}, 500

tareas_repository = TareasRepository()