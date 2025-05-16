from flask import Blueprint, render_template
from app.models import ProducaoDiaria
from datetime import datetime
from .mock_dados import *


relatorios = Blueprint('relatorios', __name__,template_folder='templates', static_folder='static')


def dia_semana_em_portugues(data):
    dias = ['seg', 'ter', 'qua', 'qui', 'sex', 'sáb', 'dom']
    # O método weekday() retorna 0 (segunda) a 6 (domingo)
    return dias[data.weekday()]

@relatorios.route("/")
def index():
    return render_template("relatorios/index.html")



@relatorios.route("/gerar_relatorio")
def gerar_relatorio():
    dias_semana = []
    dias_mes = 0
    for dia in range(1, 32):
        try:
            data = datetime(2023, 9, dia)
            dias_semana.append(dia_semana_em_portugues(data))  # 'dom', 'seg', ...
            dias_mes += 1
        except ValueError:
            break
    # dados = {
    #     "mes_ano": "09/2023",
    #     "lider": "Cleiton Xavier",
    #     "upc": "Mata Verde",
    #     "previsao": 600,
    #     "real": 530,
    #     "fornos": [
    #         {"numero": 1, "dias": ['L', 'C', 'R', 'R', 'R', 'D', 'D', 'R', 'C', 'V', 'M', 'R', 'C', 'C', 'R', 'R', 'R', 'D', 'L', 'C', 'R', 'R', 'R', 'C', 'V', 'M', 'R', 'R', 'D', 'C', 'R'], "ciclos": 3, "m3_forno": 100, "m3_total": 300},
    #         # Adicione os outros fornos aqui...
    #     ],
    #     "producao_toneladas": [2, 1, 2, 0, 3, 4, 2, 2, 2, 1, 3, 4, 3, 2, 2, 0, 1, 2, 2, 3, 2, 1, 3, 2, 1, 0, 2, 1, 0, 3, 2],
    # }
    
    
    return render_template("relatorios/relatorios.html", fornos = fornos, dias_semana=dias_semana, dias_mes=dias_mes, producao=producao,producao_re=producao_re,producao_1=producao_1, producao_2=producao_2, lenha_1=lenha_1, lenha_2=lenha_2, planejado_l=planejado_l, planejado_c=planejado_c, planejado_r=planejado_r, planejado_d=planejado_d, planejado_v=planejado_v, planejado_m=planejado_m, planejado=planejado, realizado= realizado, realizado_l=realizado_l, realizado_c=realizado_c, realizado_r=realizado_r, realizado_d=realizado_d, realizado_v=realizado_v, realizado_m=realizado_m)


@relatorios.route('/lista')
def listar_producao():
    registros = ProducaoDiaria.query.order_by(ProducaoDiaria.id).all()
    return render_template('relatorios/lista_producao.html', registros=registros)