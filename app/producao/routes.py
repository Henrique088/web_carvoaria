from flask import Blueprint, render_template

producao = Blueprint('producao', __name__,template_folder='templates', static_folder='static')

@producao.route("/")
def index():
    return render_template("producao/index.html")