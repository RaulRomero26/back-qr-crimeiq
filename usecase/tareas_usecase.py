
from repositories.tareas_repository import tareas_repository
from datetime import datetime

class TareasUsecase:

    def __init__(self, qr_repository):
        self.qr_repository = qr_repository


    def crear_tarea(self,data_tarea):
        data_tarea['fecha_asignacion'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return tareas_repository.crearTarea(data_tarea)
        

    def get_tareas(self):
        return tareas_repository.getTareas()

tareas_usecase = TareasUsecase(tareas_repository)