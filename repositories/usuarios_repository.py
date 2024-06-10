from utils.db import collection_Usu
import bcrypt
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
            data = list(collection_Usu.find({}, {'_id': 0}))
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
            update_data = {key: value for key, value in usuario_data.items() if key not in ['password', 'Foto']}
            if 'password' in usuario_data:
                password = usuario_data['password']
                hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
                update_data['password'] = hashed_password.decode('utf-8')
            if 'Foto' in usuario_data:
                update_data['Foto'] = usuario_data['Foto']
            
            collection_Usu.update_one({'_id': usuario_data['_id']}, {'$set': update_data})
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