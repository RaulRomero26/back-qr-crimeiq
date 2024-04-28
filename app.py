from flask import Flask
from flask_cors import CORS
from flask_sslify import SSLify
from routes.qr import qr
from routes.Usuarios import Login
from routes.reportes import reportes

app = Flask(__name__)
sslify = SSLify(app)

app.register_blueprint(qr)
app.register_blueprint(Login)
app.register_blueprint(reportes) 
# Configuración de CORS
CORS(app, resources={
    r"/guardar_datos": {"origins": ["*"]},
    r"/guardar_reporte": {"origins": ["*"]},
    r"/*": {"origins": "*"},  # Permitir todas las solicitudes CORS para todas las rutas
    r"/login": {"origins": ["*"]}
})

