from flask import Flask

def create_app():
    app = Flask(__name__)
    
    # Carregar configurações do config.py
    app.config.from_object('config.Config')

    # Importar e registrar os Blueprints
    from app.dashboard.routes import dashboard
    from app.fornos.routes import fornos
    from app.producao.routes import producao
    from app.operadores.routes import operadores
    from app.insumos.routes import insumos
    from app.relatorios.routes import relatorios

    app.register_blueprint(dashboard)  
    app.register_blueprint(fornos, url_prefix='/fornos')
    app.register_blueprint(producao, url_prefix='/producao')
    app.register_blueprint(operadores, url_prefix='/operadores')
    app.register_blueprint(insumos, url_prefix='/insumos')
    app.register_blueprint(relatorios, url_prefix='/relatorios')

    return app
