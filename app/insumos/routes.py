from flask import Blueprint, render_template

insumos = Blueprint('insumos', __name__,template_folder='templates', static_folder='static')

@insumos.route("/")
def index():
    return render_template("insumos/index.html")