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
    r"/guardar_datos": {"origins": ["http://127.0.0.1:5000", "http://192.168.100.31:5000", "http://192.168.100.31:5173", "http://localhost:5173"]},
    r"/guardar_reporte": {"origins": ["http://127.0.0.1:5000", "http://192.168.100.31:5000", "http://192.168.100.31:5173", "http://localhost:5173"]},
    r"/*": {"origins": "*"},  # Permitir todas las solicitudes CORS para todas las rutas
    r"/login": {"origins": ["http://127.0.0.1:5000", "http://192.168.100.31:5000", "http://192.168.100.31:5173", "http://localhost:5173"]}
})

