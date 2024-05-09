from utils.db import collection_Usu
import bcrypt
import json

class AuthRepository:

    def login(self,login_data):
        try:
            username = login_data.get('username')
            password = login_data.get('password')

            if not username or not password:
                return json.dumps({'msg': 'Falta el nombre de usuario o la contraseña'}), 400

            usuario = collection_Usu.find_one({'username': username})
            print(usuario)

            if not usuario:
                return json.dumps({'msg': 'no encontro el usuario'}), 401

            stored_password = usuario.get('password')

            # Comparar la contraseña proporcionada con la contraseña almacenada después de aplicar el hash
            if stored_password:
                check = bcrypt.checkpw(password.encode('utf-8'), stored_password.encode('utf-8'))
            else:
                return json.dumps({'msg': 'Usuario o contraseña incorrectos'}), 401

            del usuario['password']
            usuario['_id'] = str(usuario['_id'])
            if check:
                return json.dumps({'msg': 'Inicio de sesión exitoso', 'usuario': usuario}), 200
            else:
                return json.dumps({'msg': 'Usuario o contraseña incorrectos'}), 401
        except Exception as e:
            return json.dumps({'msg': str(e)}), 500

auth_repository = AuthRepository()
