from utils.db import collection_Usu
from bson import json_util
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
        
    def catalogo_tipo_tareas(self):
        try:
            data = list(collection_Usu.find({'tipo_tarea': {'$exists': True, '$ne': None}}, {'_id': 1, 'tipo_tarea': 1}))
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
    
 
    def get_catalogo(self, catalogo):
        switcher = {
            'usuarios': self.catalogo_usuarios,
            'productos': self.catalogo_tipo_tareas,
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