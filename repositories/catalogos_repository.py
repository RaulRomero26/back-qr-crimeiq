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
    
 
        
        
catalogos_repository = CatalogosRepository()