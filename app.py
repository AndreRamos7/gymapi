import random

from flask import Flask, jsonify
from flask_cors import CORS
from config import Config
from routes.upload_routes import upload_bp
import os
import math

def create_app():
    app = Flask(__name__)
    CORS(app)
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


@app.route("/sellers")
def sellers():
    vendedores = [
        "Michael Jackson", "Steve Jobs", 
        "Nancy Wheeler", "Bill Gates", 
        "Jane Hopper", "Dustin Henderson",
    ]

    return jsonify([
        {
            "vendedor": v,
            "vendas": random.randint(40, 130),
            "ticket_medio": random.randint(380, 980),
            "pct_premium": random.randint(15, 55),
            "pct_desconto": random.randint(20, 70),
            "receita": random.randint(35000, 145000)
        }
        for v in vendedores
    ])