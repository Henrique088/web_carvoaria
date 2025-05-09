# routes.py de qualquer módulo
from flask import Blueprint, render_template

login = Blueprint('login', __name__,template_folder='templates', static_folder='static', static_url_path='/login/static')

@login.route('/')
def index():
    return render_template('login/index.html')

