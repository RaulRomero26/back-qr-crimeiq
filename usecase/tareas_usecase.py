from flask import Flask, request, jsonify
from datetime import datetime
import json
import sys
import os

from repositories.tareas_repo import crearTarea, getTareas

def crear_tarea():
    try:
        # Obtener los datos del cuerpo de la solicitud como un diccionario
        data = request.get_json()
        data['fecha_asignacion'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(data)
        resultado = crearTarea(data)
        return resultado
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    

def get_tareas():
    try:
        resultado = getTareas()
        return resultado
    except Exception as e:
        return jsonify({'error': str(e)}), 500