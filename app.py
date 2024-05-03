from flask import Flask
from flask_cors import CORS
from flask_sslify import SSLify
from routes.qr import qr
from routes.Usuarios import Login
from routes.reportes import reportes
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app, origins=["http://localhost:5173", "http://example.com"])

app.register_blueprint(qr)
app.register_blueprint(Login)
app.register_blueprint(reportes)

# Configuración de SSLify
sslify = SSLify(app)
