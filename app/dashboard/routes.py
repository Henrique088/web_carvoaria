# routes.py de qualquer módulo
from flask import Blueprint, render_template

dashboard = Blueprint('dashboard', __name__,template_folder='templates', static_folder='static', static_url_path='/dashboard/static')

@dashboard.route('/')
def home():
    return render_template('dashboard/index.html')

