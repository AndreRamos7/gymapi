from flask import Flask
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
    VENDEDORES = ["Michael Jackson", "Steve Jobs", 
                  "Carla Mendes", "Bill gates", 
                  "Elaine Castro", "Felipe Nunes"];
   
    VENDEDORES.map = lambda v: {
        "vendedor": v,
        "vendas": math.floor(math.random() * (130 - 40 + 1) + 40),
        "ticket_medio": math.floor(math.random() * (980 - 380 + 1) + 380),
        "pct_premium": math.floor(math.random() * (55 - 15 + 1) + 15),
        "pct_desconto": math.floor(math.random() * (70 - 20 + 1) + 20),
        "receita": math.floor(math.random() * (145000 - 35000 + 1) + 35000)
    }
    json_response = list(map(VENDEDORES.map, VENDEDORES))
    return json_response
