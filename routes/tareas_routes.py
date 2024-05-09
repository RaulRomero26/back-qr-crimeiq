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