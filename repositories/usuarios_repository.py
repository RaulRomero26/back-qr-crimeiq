from utils.db import collection_Usu
import bcrypt
from bson import json_util, ObjectId
import json

class UsuariosRepository:

    def registrar_usuario(self, usuario_data):
        print(usuario_data)
        try:
            # Cifrar la contraseña antes de insertar los datos en la colección
            password = usuario_data.get('password')
            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

            # Actualizar el campo de contraseña con la contraseña cifrada
            usuario_data['password'] = hashed_password.decode('utf-8')

            # Insertar los datos recibidos desde la aplicación frontend en la colección
            print(usuario_data)
            collection_Usu.insert_one(usuario_data)
            return {
                'success': True,
                'message': 'Usuario registrado exitosamente.'
            }
        except Exception as e:
            return {
                'success': False,
                'error': str(e)
            }
    
    def getUsuarios(self):
        try:
            data = list(collection_Usu.find({}))
            data = json.loads(json_util.dumps(data))
            return {
                'message': 'Usuarios obtenidas exitosamente.',
                'success': True,
                'data': data
            }
        except Exception as e:
            return {
                'success': False,
                'error': str(e)
            }

    def get_usuarios_asignados(self, serv_asignado):
        try:
            data = list(collection_Usu.find({"serv_asignado": serv_asignado}, {'_id': 0, 'password': 0}))
            return {
                'message': 'Usuarios asignados obtenidos exitosamente.',
                'success': True,
                'data': data
            }
        except Exception as e:
            return {
                'success': False,
                'error': str(e)
            }
    

    def actualizar_usuario(self, usuario_data):
        try:
            # Actualizar los datos del usuario en la colección
            print('viene de inactivar:',usuario_data)
            update_data = {key: value for key, value in usuario_data.items() if key not in ['password', 'Foto','_id']}
            if 'password' in usuario_data:
                password = usuario_data['password']
                hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
                update_data['password'] = hashed_password.decode('utf-8')
            if 'Foto' in usuario_data:
                update_data['Foto'] = usuario_data['Foto']

            if usuario_data.get('activo') == 'false':
                update_data['activo'] = False
            else:
                update_data['activo'] = True  
            
            print(usuario_data.get('_id'))
            id = usuario_data.get('_id')
            id = ObjectId(id)  # Convierte la cadena a ObjectId

            collection_Usu.update_one({'_id': id}, {'$set': update_data}, upsert=True)
            return {
                'success': True,
                'message': 'Usuario actualizado exitosamente.'
            }
        except Exception as e:
            return {
                'success': False,
                'error': str(e)
            }
usuarios_repository = UsuariosRepository()