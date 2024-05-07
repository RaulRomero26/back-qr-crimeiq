from flask import Blueprint, send_from_directory, request, jsonify
from usecase.tareas_usecase import  crear_tarea, get_tareas
from utils.db import db_tareas
import os

tareas = Blueprint('tareas', __name__)

@tareas.route('/crear_tarea', methods=['POST'])
def crear_tarea_handler():
    return crear_tarea()

@tareas.route('/get-tareas', methods=['GET'])
def get_tareas_handler():
    return get_tareas()