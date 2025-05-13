from flask import Flask
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    
    # Configuração do banco de dados
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/carvoaria'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://flaskuser:senha_segura@172.30.0.1:3380/carvoaria'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    

    # Carregar configurações do config.py
    app.config.from_object('config.Config')

    # Inicializar o banco de dados
    db.init_app(app)

    # Importar e registrar os Blueprints
    from app.dashboard.routes import dashboard
    from app.fornos.routes import fornos
    from app.producao.routes import producao
    from app.operadores.routes import operadores
    from app.insumos.routes import insumos
    from app.relatorios.routes import relatorios
    from app.cadastro.routes import cadastro
    from app.login.routes import login

    app.register_blueprint(login)  # Registrar o blueprint de login
    app.register_blueprint(cadastro, url_prefix='/cadastro')  # Registrar o blueprint de cadastro
    app.register_blueprint(dashboard, url_prefix='/dashboard')  
    app.register_blueprint(fornos, url_prefix='/fornos')
    app.register_blueprint(producao, url_prefix='/producao')
    app.register_blueprint(operadores, url_prefix='/operadores')
    app.register_blueprint(insumos, url_prefix='/insumos')
    app.register_blueprint(relatorios, url_prefix='/relatorios')

    return app
