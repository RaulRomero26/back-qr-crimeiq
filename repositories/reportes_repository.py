from utils.db import collection_Inc ,collection_ale

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
    
    def guardar_alerta (self,alerta_data):
        try:
            required_fields = ['Usuario', 'fecha', 'hora','latitud', 'longitud']
            if not all(key in alerta_data for key in required_fields):
                return {'error': 'Faltan campos obligatorios en los datos recibidos'}, 400
            
            # Insertar datos en la colección de alertas
            collection_ale.insert_one(alerta_data)
            
            return {'message': 'Datos de la alerta guardados exitosamente'}, 200
        
        except KeyError as e:
                    return {'error': 'Falta el campo obligatorio: {}'.format(str(e))}, 400
                
        except Exception as e:
                return {'error': 'Error al guardar la alerta: {}'.format(str(e))}, 500
    
reportes_repository = ReportesRepository()