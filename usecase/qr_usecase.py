from flask import Flask, request, jsonify
from flask_cors import CORS
from utils.db import collection
import subprocess
import logging
import json
import sys
import os
import qrcode
from PIL import Image

def generar_qr():
    try:
        # Obtener los datos del cuerpo de la solicitud como un diccionario
        data = request.get_json()
        print(data)
        sys.stdout.flush()

        # Obtener el nombre del archivo del diccionario de datos
        nombre_archivo = data.get('nombreArchivo')  # Obtener el nombre del archivo proporcionado por el usuario

        # Validar si se proporcionó un nombre de archivo
        if not nombre_archivo:
            return jsonify({'error': 'No se proporcionó un nombre de archivo válido.'}), 400

        # Establecer la extensión del archivo de manera predeterminada a '.png'
        nombre_archivo_con_extension = f"{nombre_archivo}.png"

        # Convertir los datos a cadena JSON (opcional)
        datos_json = json.dumps(data)
        # Ruta al archivo de tu logo
        ruta_logo = "../img/3.png"  # Assuming the logo is in the same directory as the script

        # Ruta donde se guardará la imagen
        ruta_guardado = "../RESULTADO_QR"  # Assuming the directory to save the image is in the same directory as the script

        # Obtener la ruta absoluta del directorio actual
        directorio_actual = os.path.dirname(os.path.abspath(__file__))

        # Construir las rutas absolutas
        ruta_logo_absoluta = os.path.join(directorio_actual, ruta_logo)
        ruta_guardado_absoluta = os.path.join(directorio_actual, ruta_guardado)

        # Llamar al script qr.py y pasarle los datos y el nombre del archivo con extensión como argumentos
        ruta_imagen_qr = generar_codigo_qr_con_logo(datos_json, ruta_logo_absoluta, nombre_archivo_con_extension, ruta_guardado_absoluta)

        return jsonify({
            'mensaje': 'Se ha generado el código QR con éxito.',
            'ruta': ruta_imagen_qr})
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    

def generar_codigo_qr_con_logo(datos, logo_path, nombre_archivo_salida, ruta_guardado):
    try:
        # Convertir los datos a formato JSON
        datos_json = json.loads(datos)

        # Generar el código QR con los datos proporcionados
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(datos_json)
        qr.make(fit=True)

        qr_imagen = qr.make_image(fill_color="black", back_color="white")

        # Abrir el logo
        logo = Image.open(logo_path)

        # Obtener dimensiones
        qr_ancho, qr_alto = qr_imagen.size
        logo_ancho, logo_alto = logo.size

        # Calcular el ancho máximo y alto máximo para el logo (manteniendo la proporción original)
        max_ancho_logo = qr_ancho * 0.8
        max_alto_logo = qr_alto * 0.2

        # Redimensionar el logo si es necesario respetando las proporciones
        if logo_ancho > max_ancho_logo or logo_alto > max_alto_logo:
            proporcion_ancho = max_ancho_logo / logo_ancho
            proporcion_alto = max_alto_logo / logo_alto
            proporcion = min(proporcion_ancho, proporcion_alto)
            nuevo_ancho = int(logo_ancho * proporcion)
            nuevo_alto = int(logo_alto * proporcion)
            logo = logo.resize((nuevo_ancho, nuevo_alto), Image.BICUBIC)

        # Calcular la posición horizontal para centrar el logo
        posicion_x = (qr_ancho - logo.width) // 2

        # Crear una nueva imagen con el tamaño suficiente para contener el código QR y el logo
        nueva_imagen = Image.new('RGB', (qr_ancho, qr_alto + logo.height), color='white')

        # Pegar el código QR en la nueva imagen
        nueva_imagen.paste(qr_imagen, (0, 0))

        # Pegar el logo centrado horizontalmente en la parte inferior de la nueva imagen
        nueva_imagen.paste(logo, (posicion_x, qr_alto))

        # Validar y asignar la extensión del nombre de archivo
        nombre_archivo, extension = os.path.splitext(nombre_archivo_salida)
        if extension not in ['.png', '.jpg', '.jpeg']:
            nombre_archivo = nombre_archivo_salida

        # Guardar la nueva imagen en la ruta especificada
        ruta_completa = os.path.join(ruta_guardado, f"{nombre_archivo}.png")  # Asigna la extensión .png
        nueva_imagen.save(ruta_completa)

        return ruta_completa
    except Exception as e:
        return str(e)
    

def captura_qr(data):
    # Aquí puedes realizar las operaciones necesarias para capturar el QR
    try:
        # Código para insertar los datos en la base de datos, por ejemplo:
        collection.insert_one(data)
        return True
    except Exception as e:
        print(f"Error al capturar el QR: {e}")
        return False
