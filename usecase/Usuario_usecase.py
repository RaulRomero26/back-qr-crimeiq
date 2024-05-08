from flask import Flask, request, jsonify
from utils.db import db_Usu
from bson import ObjectId

def login():
    data = request.json
    UserName = data.get('username')
    password = data.get('password')
    collection = db_Usu.get_collection('USUARIOS')
    print(collection)
    if not UserName or not password:
        return jsonify({'msg': 'Falta el nombre de usuario o la contraseña'}), 400

    usuario = collection.find_one({'UserName': UserName})
    print(usuario)  # Esta línea imprimirá el objeto usuario en la consola de la aplicación Flask

    if not usuario:
        return jsonify({'msg': 'Usuario / Contraseña incorrectos'}), 400
    
    usuario['_id'] = str(usuario['_id'])

    return jsonify({'msg': 'Inicio de sesión exitoso', 'usuario': usuario}), 200
