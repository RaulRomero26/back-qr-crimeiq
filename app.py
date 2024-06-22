from flask import Flask
from flask_cors import CORS
from flask_sslify import SSLify
from flask_apscheduler import APScheduler
from routes.qr_routes import qr_routes
from routes.auth_routes import auth_routes
from routes.usuarios_routes import usuarios_routes
from routes.tareas_routes import tareas_routes
from routes.reportes_routes import reportes_routes
from routes.catalogos_routes import catalogos_routes
from jobs.jobs import job

from dotenv import load_dotenv

load_dotenv()

class Config(object):
    JOBS = [
        {
            'id': 'job1',
            'func': 'app:job',
            'trigger': 'cron',
            'hour': 7,
            'minute': 5
        }
    ]
    #'trigger': 'cron',
    #'hour': 7,
    #'minute': 0

    # 'trigger': 'interval',
    # 'hours': 10

    SCHEDULER_API_ENABLED = True


app = Flask(__name__)

# Configurar CORS
CORS(app, origins=["http://localhost:5173", "https://crimeiq.org", "https://www.crimeiq.org", "https://scanner.crimeiq.org"])

app.config.from_object(Config())

scheduler = APScheduler()
scheduler.init_app(app)
scheduler.start()

app.register_blueprint(qr_routes)
app.register_blueprint(auth_routes)
app.register_blueprint(usuarios_routes)
app.register_blueprint(tareas_routes)
app.register_blueprint(reportes_routes)
app.register_blueprint(catalogos_routes)

# Configuración de SSLify
sslify = SSLify(app)