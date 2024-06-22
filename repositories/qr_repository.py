from utils.db import collection_qr, collection_recorridos

class QrRepository:

    def capturar_qr(self, qr_data):
        try:
            collection_recorridos.insert_one(qr_data).inserted_id
            return {
                'mensaje': 'Datos guardados exitosamente',
                'success': True
            }, 200
        except Exception as e:
            return {
                    'error': str(e),
                    'success': False
                }, 500


    def generar_qr(self, qr_data):
        try:
            collection_qr.insert_one(qr_data).inserted_id
            return {
                    'mensaje': 'Se ha generado el código QR con éxito.',
                    'success': True,
                    'ruta': 'https://api.scanner.crimeiq.org/imagenes/' + qr_data['nombreArchivo']
                }, 200
        except Exception as e:
            return {
                    'error': str(e),
                    'success': False
                }, 500
        

    def obtener_qrs(self):
        try:
            data = list(collection_qr.find({}, {'_id': 0}))
            return {
                'mensaje': 'Datos obtenidos exitosamente',
                'success': True,
                'data': data
            }, 200
        except Exception as e:
            return {
                    'error': str(e),
                    'success': False
                }, 500
        
    
    def obtener_recorridos(self):
        try:
            list(collection_recorridos.find({}, {'_id': 0}))
            return {
                'mensaje': 'Datos obtenidos exitosamente',
                'success': True,
                'data': list(collection_recorridos.find({}, {'_id': 0}))
            }, 200
        except Exception as e:
            return {
                    'error': str(e),
                    'success': False
                }, 500
    
qr_repository = QrRepository()