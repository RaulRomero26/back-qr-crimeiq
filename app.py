from flask import Flask
from flask_cors import CORS
from flask_sslify import SSLify
from routes.qr_routes import qr_routes
from routes.auth_routes import auth_routes
from routes.usuarios_routes import usuarios_routes
from routes.tareas_routes import tareas_routes
from routes.reportes_routes import reportes_routes
from routes.catalogos_routes import catalogos_routes

from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Configurar CORS
CORS(app, origins=["http://localhost:5173", "https://crimeiq.org", "https://www.crimeiq.org", "https://scanner.crimeiq.org"])

app.register_blueprint(qr_routes)
app.register_blueprint(auth_routes)
app.register_blueprint(usuarios_routes)
app.register_blueprint(tareas_routes)
app.register_blueprint(reportes_routes)
app.register_blueprint(catalogos_routes)

# Configuración de SSLify
sslify = SSLify(app)
