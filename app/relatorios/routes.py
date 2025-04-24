from flask import Blueprint, render_template

relatorios = Blueprint('relatorios', __name__,template_folder='templates', static_folder='static')

@relatorios.route("/")
def index():
    return render_template("relatorios/index.html")