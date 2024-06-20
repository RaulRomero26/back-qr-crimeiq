
from repositories.tareas_repository import tareas_repository
from datetime import datetime

class TareasUsecase:

    def __init__(self, tareas_repository):
        self.tareas_repository = tareas_repository


    def crear_tarea(self,data_tarea):
        data_tarea['body']['fecha_asignacion'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return tareas_repository.crearTarea(data_tarea['body'])
        

    def get_tareas(self):
        return tareas_repository.getTareas()
    
    def get_user_tasks(self,username_id):
        return tareas_repository.get_user_tasks(username_id)
    
    def update_task_completion_date(self,task_id):
        current_date = datetime.now()
        return tareas_repository.update_task_completion_date(task_id,current_date)
    
    def get_task_recurrente(self):
        return tareas_repository.get_task_recurrente()
    
    def get_recurrent_tasks(self):
        return tareas_repository.get_recurrent_tasks()
    
    def get_recurrent_tasks(self):
        return tareas_repository.get_recurrent_tasks()
    
    def inactivar_tarea_recurrente(self,tarea_data):
        return tareas_repository.inactivar_tarea_recurrente(tarea_data)

tareas_usecase = TareasUsecase(tareas_repository)