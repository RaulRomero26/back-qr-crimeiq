from flask import Flask, request, jsonify
import json
import sys
import os

from repositories.tareas_repo import crearTarea

def crear_tarea():
    try:
        # Obtener los datos del cuerpo de la solicitud como un diccionario
        data = request.get_json()
        print(data)
        resultado = crearTarea(data)
        return resultado
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
