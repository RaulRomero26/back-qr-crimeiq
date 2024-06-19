from flask import Blueprint, request, jsonify
from usecase.tareas_usecase import tareas_usecase

tareas_routes = Blueprint('tareas_routes', __name__)

@tareas_routes.route('/crear_tarea', methods=['POST'])
def crear_tarea():
    tarea_data = request.get_json()
    return tareas_usecase.crear_tarea(tarea_data)

@tareas_routes.route('/all-tareas')
def get_tareas():
    return tareas_usecase.get_tareas()

@tareas_routes.route('/get_user_tasks', methods=['POST'])
def get_user_tasks():
    user_data = request.json
    username_id = user_data.get('username_id')
    return tareas_usecase.get_user_tasks(username_id)

@tareas_routes.route('/update_task_completion_date', methods=['POST'])
def update_task_completion_date():
    data = request.json
    task_id = data.get('task_id')
    return tareas_usecase.update_task_completion_date(task_id)

@tareas_routes.route('/get_task_recurrente')
def get_task_recurrente():
    return tareas_usecase.get_task_recurrente()

@tareas_routes.route('/inactivar_tarea_recurrente', methods=['POST'])
def inactivar_tarea_recurrente():
    tarea_data = request.json
    return tareas_usecase.inactivar_tarea_recurrente(tarea_data)