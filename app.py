from flask import Flask
from config import Config
from routes.upload_routes import upload_bp
import os

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Criar pasta uploads se não existir
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

    # Registrar blueprints
    app.register_blueprint(upload_bp, url_prefix="/api")

    return app


app = create_app()
#app.run(debug=False, port=5001) run é para desenvolvimento, em produção use um servidor como gunicorn ou uwsgi

@app.route("/")
def hello_world():
    return "<p>Hello, Worlds!</p>"

@app.route("/cluster")
def cluster():
    return "<p>Hello, Cluster!</p>"

@app.route("/prevision")
def prevision():
    return "<p>Hello, Prevision!</p>"