from pymongo import MongoClient
import os

class Database:
    def __init__(self, uri, db_name):
        self.client = MongoClient(uri)
        self.db = self.client[db_name]

    def get_collection(self, collection_name):
        return self.db[collection_name]

# Configuración de la base de datos MongoDB
MONGO_URI = os.getenv('MONGO_URI')  # URI de conexión a MongoDB

class MyDatabase:
    def __init__(self, db_name):
        self.db = Database(MONGO_URI, db_name)

    def get_collection(self, collection_name):
        return self.db.get_collection(collection_name)

# Crear una instancia de la base de datos
db = MyDatabase('REGISTROS_QR')
collection_recorridos = db.get_collection('RECORRIDOS')
collection_qr = db.get_collection('QR_CREADOS')

db_Usu = MyDatabase('USU_CIQ')
collection_Usu = db_Usu.get_collection('USUARIOS')

db_Inc = MyDatabase('REP_INCIDENCIA')
collection_Inc = db_Inc.get_collection('INCIDENCIAS')
collection_ale = db_Inc.get_collection('ALERTAS')

db_tareas = MyDatabase('TAREAS')
collection_tareas = db_tareas.get_collection('TAREAS')
