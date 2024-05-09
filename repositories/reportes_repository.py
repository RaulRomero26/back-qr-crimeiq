from utils.db import collection_Inc

class ReportesRepository:

    def guardar_reporte(reporte_data):
        try:
            # Insertar los datos recibidos desde la aplicación frontend en la colección
            collection_Inc.insert_one(reporte_data)
            return {
                    'success': True, 
                    'message': 'Reporte creado exitosamente.'
                    }
        except Exception as e:
            return {
                    'success': False, 
                    'error': str(e)
                }
        
    
    def getReportes():
        try:
            data = list(collection_Inc.find({}, {'_id': 0}))
            return {
                'message': 'Reportes exitosamente.',
                'success': True,
                'data': data
            }
        except Exception as e:
            return {
                'success': False,
                'error': str(e)
            }
    
reportes_repository = ReportesRepository()