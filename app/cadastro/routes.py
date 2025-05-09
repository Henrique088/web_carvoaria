# routes.py de qualquer módulo
from flask import Blueprint, render_template

cadastro = Blueprint('cadastro', __name__,template_folder='templates', static_folder='static', static_url_path='/cadastro/static')

@cadastro.route('/')
def index():
    return render_template('cadastro/index.html')

