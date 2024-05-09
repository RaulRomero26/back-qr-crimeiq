from repositories.qr_repository import qr_repository
import os
import json
import qrcode
from PIL import Image

class QrUsecase:
    def __init__(self, qr_repository):
        self.qr_repository = qr_repository

    def generar_qr(self, qr_data):
        try:
            qr_data = qr_data['body']            
            nombre_archivo = qr_data.get('nombreArchivo')
            if not nombre_archivo:
                return {'error': 'No se proporcionó un nombre de archivo válido.'}, 400
            
            nombre_archivo_con_extension = f"{nombre_archivo}.png"

            ruta_logo = "../Img/3.png"
            ruta_guardado = "../RESULTADO_QR"
            directorio_actual = os.path.dirname(os.path.abspath(__file__))

            ruta_logo_absoluta = os.path.abspath(os.path.join(directorio_actual, ruta_logo))
            ruta_guardado_absoluta = os.path.abspath(os.path.join(directorio_actual, ruta_guardado))

            ruta_imagen_qr = self.generar_codigo_qr_con_logo(json.dumps(qr_data), ruta_logo_absoluta, nombre_archivo_con_extension, ruta_guardado_absoluta)

            qr_data['ruta_imagen_qr'] = 'http://localhost:5000/imagenes/' + nombre_archivo_con_extension
            return self.qr_repository.generar_qr(qr_data)

        except Exception as e:
            return {'error': str(e)}, 500
        

    def generar_codigo_qr_con_logo(self, datos, logo_path, nombre_archivo_salida, ruta_guardado):
        try:
            datos_json = json.loads(datos)

            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            qr.add_data(datos_json)
            qr.make(fit=True)

            qr_imagen = qr.make_image(fill_color="black", back_color="white")

            logo = Image.open(logo_path)

            qr_ancho, qr_alto = qr_imagen.size
            logo_ancho, logo_alto = logo.size

            max_ancho_logo = qr_ancho * 0.8
            max_alto_logo = qr_alto * 0.2

            if logo_ancho > max_ancho_logo or logo_alto > max_alto_logo:
                proporcion_ancho = max_ancho_logo / logo_ancho
                proporcion_alto = max_alto_logo / logo_alto
                proporcion = min(proporcion_ancho, proporcion_alto)
                nuevo_ancho = int(logo_ancho * proporcion)
                nuevo_alto = int(logo_alto * proporcion)
                logo = logo.resize((nuevo_ancho, nuevo_alto), Image.BICUBIC)

            posicion_x = (qr_ancho - logo.width) // 2

            nueva_imagen = Image.new('RGB', (qr_ancho, qr_alto + logo.height), color='white')

            nueva_imagen.paste(qr_imagen, (0, 0))
            nueva_imagen.paste(logo, (posicion_x, qr_alto))

            nombre_archivo, extension = os.path.splitext(nombre_archivo_salida)
            if extension not in ['.png', '.jpg', '.jpeg']:
                nombre_archivo = nombre_archivo_salida

            ruta_completa = os.path.join(ruta_guardado, f"{nombre_archivo}.png")
            nueva_imagen.save(ruta_completa)

            return ruta_completa
        except Exception as e:
            return str(e)
    
    def capturar_qr(self, qr_data):
        return self.qr_repository.capturar_qr(qr_data)
    
    def obtener_qrs(self):
        return self.qr_repository.obtener_qrs()
    
    def obtener_recorridos(self):
        return self.qr_repository.obtener_recorridos()
    
qr_usecase = QrUsecase(qr_repository)