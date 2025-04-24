from flask import Blueprint, render_template


fornos = Blueprint('fornos', __name__,template_folder='templates', static_folder='static')

@fornos.route("/")
def index():
    return render_template("fornos/index.html")