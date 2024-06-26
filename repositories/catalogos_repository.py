from utils.db import collection_Usu,db_catatalogos
from bson import json_util, ObjectId
import json

class CatalogosRepository:

    
    def catalogo_usuarios(self):
        try:
            data = list(collection_Usu.find({'username': {'$exists': True, '$ne': None}}, {'_id': 1, 'username': 1}))
            data = json.loads(json_util.dumps(data))
            return {
                'message': 'Usuarios Obtenidos exitosamente.',
                'success': True,
                'data': data
            }
        except Exception as e:
            return {
                'success': False,
                'error': str(e)
            }
        

    def catalogo_roles(self):
        try:
            collection = db_catatalogos.get_collection('ROLES')
            data = list(collection.find({'role': {'$exists': True, '$ne': None}}, {'_id': 1, 'role': 1, 'activo': 1}))
            data = json.loads(json_util.dumps(data))
            return {
                'message': 'Roles Obtenidos exitosamente.',
                'success': True,
                'data': data
            }
        except Exception as e:
            return {
                'success': False,
                'error': str(e)
            }
        
    def catalogo_tipo_tareas(self):
        try:
            
            collection = db_catatalogos.get_collection('ACTIVIDADES')
            data = list(collection.find({'actividad': {'$exists': True, '$ne': None}}, {'_id': 1, 'actividad': 1, 'activo': 1}))
            data = json.loads(json_util.dumps(data))
            return {
                'message': 'Tipo de tareas Obtenidos exitosamente.',
                'success': True,
                'data': data
            }
        except Exception as e:
            return {
                'success': False,
                'error': str(e)
            }
        
    def catalogo_servicios(self):
        try:
            collection = db_catatalogos.get_collection('SERVICIOS')
            data = list(collection.find({'servicio': {'$exists': True, '$ne': None}}, {'_id': 1, 'servicio': 1, 'direccion': 1, 'activo': 1}))
            data = json.loads(json_util.dumps(data))
            return {
                'message': 'Servicios Obtenidos exitosamente.',
                'success': True,
                'data': data
            }
        except Exception as e:
            return {
                'success': False,
                'error': str(e)
            }
    
    def update_roles(self, catalogo_data):
        try:
            collection = db_catatalogos.get_collection('ROLES')
            id = catalogo_data.get('_id').get('$oid')  # Accede a $oid
            id = ObjectId(id)  # Convierte la cadena a ObjectId
            collection.update_one({'_id': id}, {'$set': {'role': catalogo_data.get('role'), 'activo': catalogo_data.get('activo')}})
            return {
                'message': 'Rol actualizado exitosamente.',
                'success': True
            }
        except Exception as e:
            return {
                'success': False,
                'error': str(e)
            }

    def update_tipo_tareas(self, catalogo_data):
        try:
            collection = db_catatalogos.get_collection('ACTIVIDADES')
            id = catalogo_data.get('_id').get('$oid')  # Accede a $oid
            id = ObjectId(id)  # Convierte la cadena a ObjectId
            collection.update_one({'_id': id}, {'$set': {'actividad': catalogo_data.get('actividad'), 'activo': catalogo_data.get('activo')}})
            return {
                'message': 'Tipo de tarea actualizado exitosamente.',
                'success': True
            }
        except Exception as e:
            return {
                'success': False,
                'error': str(e)
            }
        
    def update_servicios(self, catalogo_data):
        try:
            collection = db_catatalogos.get_collection('SERVICIOS')
            id = catalogo_data.get('_id').get('$oid')  # Accede a $oid
            id = ObjectId(id)  # Convierte la cadena a ObjectId
            collection.update_one({'_id': id}, {'$set': {'servicio': catalogo_data.get('servicio'), 'activo': catalogo_data.get('activo')}})
            return {
                'message': 'Servicio actualizado exitosamente.',
                'success': True
            }
        except Exception as e:
            return {
                'success': False,
                'error': str(e)
            }
 
    def add_option_roles(self, catalogo_data):
        try:
            collection = db_catatalogos.get_collection('ROLES')
            collection.insert_one({'role': catalogo_data.get('role'), 'activo': catalogo_data.get('activo')})
            return {
                'message': 'Rol agregado exitosamente.',
                'success': True
            }
        except Exception as e:
            return {
                'success': False,
                'error': str(e)
            }

    def add_option_tipo_tareas(self, catalogo_data):
        try:
            collection = db_catatalogos.get_collection('ACTIVIDADES')
            collection.insert_one({'actividad': catalogo_data.get('actividad'), 'activo': catalogo_data.get('activo')})
            return {
                'message': 'Tipo de tarea agregado exitosamente.',
                'success': True
            }
        except Exception as e:
            return {
                'success': False,
                'error': str(e)
            }

    def add_option_servicios(self, catalogo_data):
        try:
            collection = db_catatalogos.get_collection('SERVICIOS')
            collection.insert_one({'servicio': catalogo_data.get('servicio'), 'direccion': catalogo_data.get('direccion'), 'activo': catalogo_data.get('activo')})
            return {
                'message': 'Servicio agregado exitosamente.',
                'success': True
            }
        except Exception as e:
            return {
                'success': False,
                'error': str(e)
            }

    def get_catalogo(self, catalogo):
        print('Catalogo:', catalogo)
        switcher = {
            'roles-usuarios': self.catalogo_roles,
            'tipos-tareas': self.catalogo_tipo_tareas,
            'servicios': self.catalogo_servicios,
            # Agrega más aquí si es necesario
        }
        
        # Obtén la función del diccionario
        func = switcher.get(catalogo)

        # Si la función existe, llámala
        if func:
            return func()
        else:
            return 'Catálogo no encontrado'


    def update_catalogo(self, catalogo_data):
        print(catalogo_data)
        switcher = {
            'roles-usuarios': self.update_roles,
            'tipos-tareas': self.update_tipo_tareas,
            'servicios': self.update_servicios,
            # Agrega más aquí si es necesario
        } 

        func = switcher.get(catalogo_data.get('catalogo'))

        if func:
            return func(catalogo_data)
        else:
            return 'Catálogo no encontrado'
        
    def add_option(self, catalogo_data):
        switcher = {
            'roles-usuarios': self.add_option_roles,
            'tipos-tareas': self.add_option_tipo_tareas,
            'servicios': self.add_option_servicios,
            # Agrega más aquí si es necesario
        }

        func = switcher.get(catalogo_data.get('catalogo'))

        if func:
            return func(catalogo_data)
        else:
            return 'Catálogo no encontrado'

    def catalogo_roles_activos(self):
        try:
            collection = db_catatalogos.get_collection('ROLES')
            data = list(collection.find({'role': {'$exists': True, '$ne': None}, 'activo': True}, {'_id': 1, 'role': 1}))
            data = json.loads(json_util.dumps(data))
            return {
                'message': 'Roles Obtenidos exitosamente.',
                'success': True,
                'data': data
            }
        except Exception as e:
            return {
                'success': False,
                'error': str(e)
            }
    
    def catalogo_tipo_tareas_activos(self):
        try:
            collection = db_catatalogos.get_collection('ACTIVIDADES')
            data = list(collection.find({'actividad': {'$exists': True, '$ne': None}, 'activo': True}, {'_id': 1, 'actividad': 1}))
            data = json.loads(json_util.dumps(data))
            return {
                'message': 'Tipo de tareas Obtenidos exitosamente.',
                'success': True,
                'data': data
            }
        except Exception as e:
            return {
                'success': False,
                'error': str(e)
            }

    def catalogo_servicios_activos(self):
        try:
            collection = db_catatalogos.get_collection('SERVICIOS')
            data = list(collection.find({'servicio': {'$exists': True, '$ne': None}, 'activo': True}, {'_id': 1, 'servicio': 1, 'direccion': 1}))
            data = json.loads(json_util.dumps(data))
            return {
                'message': 'Servicios Obtenidos exitosamente.',
                'success': True,
                'data': data
            }
        except Exception as e:
            return {
                'success': False,
                'error': str(e)
            }

    def catalogo_usuarios_activos(self):
        try:
            data = list(collection_Usu.find({'username': {'$exists': True, '$ne': None}}, {'_id': 1, 'username': 1}))
            data = json.loads(json_util.dumps(data))
            return {
                'message': 'Usuarios Obtenidos exitosamente.',
                'success': True,
                'data': data
            }
        except Exception as e:
            return {
                'success': False,
                'error': str(e)
            }
    
    def catalogo_servicios_activos(self):
        try:
            collection = db_catatalogos.get_collection('SERVICIOS')
            data = list(collection.find({'servicio': {'$exists': True, '$ne': None}, 'activo': True}, {'_id': 1, 'servicio': 1, 'direccion': 1}))
            data = json.loads(json_util.dumps(data))
            return {
                'message': 'Servicios Obtenidos exitosamente.',
                'success': True,
                'data': data
            }
        except Exception as e:
            return {
                'success': False,
                'error': str(e)
            }

    def get_catalogo_activos(self,catalogo):
        print('Catalogo:', catalogo)
        switcher = {
            'roles-usuarios': self.catalogo_roles_activos,
            'tipos-tareas': self.catalogo_tipo_tareas_activos,
            'servicios': self.catalogo_servicios_activos,
            'usuarios': self.catalogo_usuarios_activos,
            # Agrega más aquí si es necesario
        }
        
        # Obtén la función del diccionario
        func = switcher.get(catalogo)

        # Si la función existe, llámala
        if func:
            return func()
        else:
            return 'Catálogo no encontrado'
        
catalogos_repository = CatalogosRepository()