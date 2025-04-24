from flask import Blueprint, render_template

operadores = Blueprint('operadores', __name__,template_folder='templates', static_folder='static')

@operadores.route("/")
def index():
    return render_template("operadores/index.html")