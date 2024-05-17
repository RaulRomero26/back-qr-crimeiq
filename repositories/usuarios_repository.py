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
    
usuarios_repository = UsuariosRepository()