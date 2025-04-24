# routes.py de qualquer módulo
from flask import Blueprint, render_template

dashboard = Blueprint('dashboard', __name__,template_folder='templates', static_folder='static')

@dashboard.route('/')
def home():
    import os
    print("Caminho templates:", os.path.abspath('templates'))
    return render_template('dashboard/index.html')

