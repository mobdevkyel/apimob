import pandas as pd
from flask import Flask, jsonify, redirect, render_template, url_for, request
import requests


app = Flask(__name__)

@app.route('/')
def inicial():
    return 'API no ar'

@app.route('/speedway')
def speedway():
    teste = {"nome": "ezequiel"}
    return jsonify(teste)

@app.route('/taxaspeedway', methods=['POST'])
def speedway_taxa():
    tp = request.form.get('tempo')

    tempo = tp
    hora = True
    sql = ""

    if hora:
        sql = f"""
                    SELECT `id`, `vencedorNumero`, `dataHora` 
                    FROM `speedway_resultados` 
                    WHERE STR_TO_DATE(CONCAT(`dataHora`), '%d-%m-%Y %H:%i:%s') >= DATE(SUBDATE(NOW(), INTERVAL {tempo} HOUR))
                    #WHERE 1
                    order by 1 desc
                """
    else:
        sql = """
                    SELECT `id`, `vencedorNumero`, `dataHora` 
                    FROM `speedway_resultados` 
                    WHERE 1
                    order by 1 desc
                """

    url3 = 'http://mobtrader.atwebpages.com/api/ultimos_3.php'
    respp = requests.get(url3)
    dads = respp.json()

    pilotos = f"{dads['Cores'][0]['Numero']}{dads['Cores'][1]['Numero']}{dads['Cores'][2]['Numero']}"
    #print(pilotos)

    url = 'http://mobtrader.atwebpages.com/api/retorno.php'
    info = {"consulta": sql}
    resp = requests.post(url, info)
    dados = resp.json()

    padrao = pilotos

    duplas_geral = [1, 2, 3, 4]

    resultatos = {}

    r = []
    r2 = ''

    vermelho = 0
    verde = 0
    amarele = 0
    roxo = 0

    count = 0

    df = pd.DataFrame(dados)

    for i in df["vencedorNumero"]:
        count += 1
        r.append(i)
    r.reverse()
    r2 = str(r).strip('[]').replace("'", "").replace(", ", "")

    verde_win = 0
    vermelho_win = 0
    amarelo_win = 0
    roxo_win = 0

    G1_verde = 0
    G1_vermelho = 0
    G1_amarelo = 0
    G1_roxo = 0

    G2_verde = 0
    G2_vermelho = 0
    G2_amarelo = 0
    G2_roxo = 0

    win = []

    verde_g1 = []
    verde_g2 = []

    vermelho_g1 = []
    vermelho_g2 = []

    amarelo_g1 = []
    amarelo_g2 = []

    roxo_g1 = []
    roxo_g2 = []

    ct = 0
    for item in duplas_geral:
        ct += 1
        dupla = str(item)
        padraos = f'{padrao}{dupla}'
        win.append(padraos)
        contagem = (r2.count(f'{padraos}'))
        contagem = int(contagem)
        corredor = int(padraos[-1:])
        if corredor == 1:
            verde_win = contagem
        elif corredor == 2:
            vermelho_win = contagem
        elif corredor == 3:
            amarelo_win = contagem
        elif corredor == 4:
            roxo_win = contagem

    verde_g1.append(f'{win[0]}1')
    verde_g1.append(f'{win[0]}2')
    verde_g1.append(f'{win[0]}3')
    verde_g1.append(f'{win[0]}4')
    for i in verde_g1:
        contagem = (r2.count(f'{i}'))
        contagem = int(contagem)
        corredor = int(i[-1:])
        if corredor == 1:
            G1_verde = contagem
        elif corredor == 2:
            G1_vermelho = contagem
        elif corredor == 3:
            G1_amarelo = contagem
        elif corredor == 4:
            G1_roxo = contagem

    verde_g2.append(f'{verde_g1[0]}1')
    verde_g2.append(f'{verde_g1[0]}2')
    verde_g2.append(f'{verde_g1[0]}3')
    verde_g2.append(f'{verde_g1[0]}4')
    for i in verde_g2:
        contagem = (r2.count(f'{i}'))
        contagem = int(contagem)
        corredor = int(i[-1:])
        if corredor == 1:
            G2_verde = contagem
        elif corredor == 2:
            G2_vermelho = contagem
        elif corredor == 3:
            G2_amarelo = contagem
        elif corredor == 4:
            G2_roxo = contagem

    vermelho_g1.append(f'{win[1]}1')
    vermelho_g1.append(f'{win[1]}2')
    vermelho_g1.append(f'{win[1]}3')
    vermelho_g1.append(f'{win[1]}4')
    for i in vermelho_g1:
        contagem = (r2.count(f'{i}'))
        contagem = int(contagem)
        corredor = int(i[-1:])
        if corredor == 1:
            G1_verde = contagem
        elif corredor == 2:
            G1_vermelho = contagem
        elif corredor == 3:
            G1_amarelo = contagem
        elif corredor == 4:
            G1_roxo = contagem

    vermelho_g2.append(f'{vermelho_g1[1]}1')
    vermelho_g2.append(f'{vermelho_g1[1]}2')
    vermelho_g2.append(f'{vermelho_g1[1]}3')
    vermelho_g2.append(f'{vermelho_g1[1]}4')
    for i in vermelho_g2:
        contagem = (r2.count(f'{i}'))
        contagem = int(contagem)
        corredor = int(i[-1:])
        if corredor == 1:
            G2_verde = contagem
        elif corredor == 2:
            G2_vermelho = contagem
        elif corredor == 3:
            G2_amarelo = contagem
        elif corredor == 4:
            G2_roxo = contagem

    amarelo_g1.append(f'{win[2]}1')
    amarelo_g1.append(f'{win[2]}2')
    amarelo_g1.append(f'{win[2]}3')
    amarelo_g1.append(f'{win[2]}4')
    for i in amarelo_g1:
        contagem = (r2.count(f'{i}'))
        contagem = int(contagem)
        corredor = int(i[-1:])
        if corredor == 1:
            G1_verde = contagem
        elif corredor == 2:
            G1_vermelho = contagem
        elif corredor == 3:
            G1_amarelo = contagem
        elif corredor == 4:
            G1_roxo = contagem

    amarelo_g2.append(f'{amarelo_g1[2]}1')
    amarelo_g2.append(f'{amarelo_g1[2]}2')
    amarelo_g2.append(f'{amarelo_g1[2]}3')
    amarelo_g2.append(f'{amarelo_g1[2]}4')
    for i in amarelo_g2:
        contagem = (r2.count(f'{i}'))
        contagem = int(contagem)
        corredor = int(i[-1:])
        if corredor == 1:
            G2_verde = contagem
        elif corredor == 2:
            G2_vermelho = contagem
        elif corredor == 3:
            G2_amarelo = contagem
        elif corredor == 4:
            G2_roxo = contagem

    roxo_g1.append(f'{win[3]}1')
    roxo_g1.append(f'{win[3]}2')
    roxo_g1.append(f'{win[3]}3')
    roxo_g1.append(f'{win[3]}4')
    for i in roxo_g1:
        contagem = (r2.count(f'{i}'))
        contagem = int(contagem)
        corredor = int(i[-1:])
        if corredor == 1:
            G1_verde = contagem
        elif corredor == 2:
            G1_vermelho = contagem
        elif corredor == 3:
            G1_amarelo = contagem
        elif corredor == 4:
            G1_roxo = contagem

    roxo_g2.append(f'{roxo_g1[3]}1')
    roxo_g2.append(f'{roxo_g1[3]}2')
    roxo_g2.append(f'{roxo_g1[3]}3')
    roxo_g2.append(f'{roxo_g1[3]}4')
    for i in roxo_g2:
        contagem = (r2.count(f'{i}'))
        contagem = int(contagem)
        corredor = int(i[-1:])
        if corredor == 1:
            G2_verde = contagem
        elif corredor == 2:
            G2_vermelho = contagem
        elif corredor == 3:
            G2_amarelo = contagem
        elif corredor == 4:
            G2_roxo = contagem

    resultatos["Verde"] = verde_win
    resultatos["Verde G1"] = G1_verde
    resultatos["Verde G2"] = G2_verde
    resultatos["Vermelho"] = vermelho_win
    resultatos["Vermelho G1"] = G1_vermelho
    resultatos["Vermelho G2"] = G2_vermelho
    resultatos["Amarelo"] = amarelo_win
    resultatos["Amarelo G1"] = G1_amarelo
    resultatos["Amarelo G2"] = G2_amarelo
    resultatos["Roxo"] = roxo_win
    resultatos["Roxo G1"] = G1_roxo
    resultatos["Roxo G2"] = G2_roxo

    total_pilotos = verde_win + vermelho_win + amarelo_win + roxo_win + G1_verde + G1_vermelho + G1_amarelo + G1_roxo + G2_verde + G2_vermelho + G2_amarelo + G2_roxo
    pverde = round((verde_win * 100) / total_pilotos, 2)
    pvermelho = round((vermelho_win * 100) / total_pilotos, 2)
    pamarelo = round((amarelo_win * 100) / total_pilotos, 2)
    proxo = round((roxo_win * 100) / total_pilotos, 2)

    pverdeg1 = round(((G1_verde) * 100) / total_pilotos, 2)
    pvermelhog1 = round((G1_vermelho * 100) / total_pilotos, 2)
    pamarelog1 = round((G1_amarelo * 100) / total_pilotos, 2)
    proxog1 = round((G1_roxo * 100) / total_pilotos, 2)

    pverdeg2 = round(((G2_verde) * 100) / total_pilotos, 2)
    pvermelhog2 = round((G2_vermelho * 100) / total_pilotos, 2)
    pamarelog2 = round((G2_amarelo * 100) / total_pilotos, 2)
    proxog2 = round((G2_roxo * 100) / total_pilotos, 2)

    tpverde = round(pverde + pverdeg1 + pverdeg2, 2)
    tpvermelho = round(pvermelho + pvermelhog1 + pvermelhog2, 2)
    tpamarelo = round(pamarelo + pamarelog1 + pamarelog2, 2)
    tparoxo = round(proxo + proxog1 + proxog2, 2)

    VERDE_VERMELHO = round(tpverde + tpvermelho, 2)
    VERDE_AMARELO = round(tpverde + tpamarelo, 2)
    VERDE_ROXO = round(tpverde + tparoxo, 2)

    VERMELHO_VERDE = round(tpvermelho + tpverde, 2)
    VERMELHO_AMARELO = round(tpvermelho + tpamarelo, 2)
    VERMELHO_ROXO = round(tpvermelho + tparoxo, 2)

    AMARELO_VERDE = round(tpamarelo + tpverde, 2)
    AMARELO_VERMELHO = round(tpamarelo + tpvermelho, 2)
    AMARELO_ROXO = round(tpamarelo + tparoxo, 2)

    ROXO_VERDE = round(tparoxo + tpverde, 2)
    ROXO_VERMELHO = round(tparoxo + tpvermelho, 2)
    ROXO_AMARELO = round(tparoxo + tpamarelo, 2)

    t = VERDE_VERMELHO + VERDE_AMARELO + VERDE_ROXO + VERDE_ROXO + VERMELHO_AMARELO + VERMELHO_ROXO + AMARELO_VERDE + AMARELO_VERMELHO + AMARELO_ROXO + ROXO_VERDE + ROXO_VERMELHO + ROXO_AMARELO
    VERDEVERMELHO = round((VERDE_VERMELHO * 100) / t)
    VERDEAMARELO = round((VERDE_AMARELO * 100) / t)
    VERDEROXO = round((VERDE_ROXO * 100) / t)
    VERMELHOVERDE = round((VERMELHO_VERDE * 100) / t)
    VERMELHOAMARELO = round((VERMELHO_AMARELO * 100) / t)
    VERMELHOROXO = round((VERMELHO_ROXO * 100) / t)
    AMARELOVERDE = round((AMARELO_VERDE * 100) / t)
    AMARELOVERMELHO = round((AMARELO_VERMELHO * 100) / t)
    AMARELOROXO = round((AMARELO_ROXO * 100) / t)
    ROXOVERDE = round((ROXO_VERDE * 100) / t)
    ROXOVERMELHO = round((ROXO_VERMELHO * 100) / t)
    ROXOAMARELO = round((ROXO_AMARELO * 100) / t)

    g = (f'''
        Total {total_pilotos}
        VERDE    - WIN = {pverde}% / G1 = {pverdeg1}% / G2 = {pverdeg2}% / TAXA = {tpverde}%
        VERMELHO - WIN = {pvermelho}% / G1 = {pvermelhog1}% / G2 = {pvermelhog2}% / TAXA = {tpvermelho}%
        AMARELO  - WIN = {pamarelo}% / G1 = {pamarelog1}% / G2 = {pamarelog2}% / TAXA = {tpamarelo}%
        ROXO     - WIN = {proxo}% / G1 = {proxog1}% / G2 = {proxog2}% / TAXA = {tparoxo}%

        VERDE/VERMELHO   = {VERDE_VERMELHO}%   = {VERDEVERMELHO}%
        VERDE/AMARELO    = {VERDE_AMARELO}%    = {VERDEAMARELO}%
        VERDE/ROXO       = {VERDE_ROXO}%       = {VERDEROXO}%

        VERMELHO/VERDE   = {VERMELHO_VERDE}%   = {VERMELHOVERDE}%
        VERMELHO/AMARELO = {VERMELHO_AMARELO}% = {VERMELHOAMARELO}%
        VERMELHO/ROXO    = {VERMELHO_ROXO}%    = {VERMELHOROXO}%

        AMARELO/VERDE    = {AMARELO_VERDE}%    = {AMARELOVERDE}%
        AMARELO/VERMELHO = {AMARELO_VERMELHO}% = {AMARELOVERMELHO}%
        AMARELO/ROXO     = {AMARELO_ROXO}%     = {AMARELOROXO}%

        ROXO/VERDE       = {ROXO_VERDE}%       = {ROXOVERDE}%
        ROXO/VERMELHO    = {ROXO_VERMELHO}%    = {ROXOVERMELHO}%
        ROXO/AMARELO     = {ROXO_AMARELO}%     = {ROXOAMARELO}%

            ''')

    retorno = {
        "VERDE/VERMELHO"   : VERDE_VERMELHO,
        "VERDE/AMARELO"    : VERDE_AMARELO,
        "VERDE/ROXO"       : VERDE_ROXO,

        "VERMELHO/VERDE"   : VERMELHO_VERDE,
        "VERMELHO/AMARELO" : VERMELHO_AMARELO,
        "VERMELHO/ROXO"    : VERMELHO_ROXO,

        "AMARELO/VERDE"   : AMARELO_VERDE,
        "AMARELO/VERMELHO": AMARELO_VERMELHO,
        "AMARELO/ROXO"    : AMARELO_ROXO,

        "ROXO/VERDE"      : ROXO_VERDE,
        "ROXO/VERMELHO"   : ROXO_VERMELHO,
        "ROXO/AMARELO"    : ROXO_AMARELO
    }


    return jsonify(retorno)





if __name__ == "__main__":
    app.run()
