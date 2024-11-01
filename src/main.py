from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from controllers.rotas import app  # Importa as rotas
from config import config
from models.models import db  # Supondo que você tenha um arquivo models.py onde o db é definido

# Configuração das pastas contendo HTML => views/templates e CSS => views/static
aplicativo = Flask(__name__, template_folder='views/templates/', static_folder='views/static')

# Este arquivo serve para armazenar toda a configuração do projeto em um único lugar
# para facilitar a configuração
config.configuracao(aplicativo)  # Configuração deve ser chamada antes de inicializar o db

# Inicializa o SQLAlchemy com a aplicação
db.init_app(aplicativo)  # Aqui você deve passar 'aplicativo' para inicializar corretamente

# Registra o blueprint das rotas
aplicativo.register_blueprint(app)

# Cria o banco se não existir
with aplicativo.app_context():
    db.create_all()  # Isso cria as tabelas definidas nos modelos

# para subir este projeto no docker, mude o host e a porta  host='0.0.0.0' e port='8080'
if __name__ == '__main__':
    aplicativo.run(host='127.0.0.1', port=5000, debug=True)
