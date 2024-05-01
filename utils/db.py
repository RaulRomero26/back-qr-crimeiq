from pymongo import MongoClient

class Database:
    def __init__(self, uri, db_name):
        self.client = MongoClient(uri)
        self.db = self.client[db_name]

    def get_collection(self, collection_name):
        return self.db[collection_name]

# Configuración de la base de datos MongoDB
MONGO_URI = 'mongodb://crimeiq:admincrimeiq@178.16.142.22:27319/?authMechanism=DEFAULT&authSource=admin'  # URI de conexión a MongoDB
DB_NAME = 'REGISTROS_QR'  # Nombre de tu base de datos en MongoDB
COLLECTION_NAME = 'RECORRIDOS'  # Nombre de tu colección en MongoDB

# Crear una instancia de la base de datos
db = Database(MONGO_URI, DB_NAME)
collection = db.get_collection(COLLECTION_NAME)

DB_NAME_USER = 'USU_CIQ'  # Nombre de tu base de datos en MongoDB
COLLECTION_NAME_USER = 'USUARIOS'  # Nombre de tu colección en MongoDB

# Crear una instancia de la base de datos
db_Usu = Database(MONGO_URI, DB_NAME_USER)
collection_Usu = db_Usu.get_collection(COLLECTION_NAME_USER)


DB_NAME_REPO = 'REP_INCIDENCIA'  # Nombre de tu base de datos en MongoDB
COLLECTION_NAME_REPO = 'INCIDENCIAS'  # Nombre de tu colección en MongoDB

# Crear una instancia de la base de datos
db_Inc = Database(MONGO_URI, DB_NAME_REPO)
collection_Inc = db_Inc.get_collection(COLLECTION_NAME_REPO)
