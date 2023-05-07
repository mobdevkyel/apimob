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

@app.route('/galgoshillside', methods=['POST', 'GET'])
def galgoshillside():
    def numeros(tricast):
        
        numeros_possiveis = [1, 2, 3, 4, 5, 6]

        # converter a string do tricast em uma lista de inteiros
        numeros_tricast = [int(num) for num in tricast.split("-")]

        # criar uma nova lista com os números que não aparecem no tricast
        numeros_faltantes = [num for num in numeros_possiveis if num not in numeros_tricast]

        # ordenar a nova lista em ordem crescente
        numeros_faltantes.sort()

        return numeros_faltantes

    # URL do arquivo PHP que retorna o JSON
    url = "https://mobblaze.000webhostapp.com/api_fb/galgohillside.php"

    # Realiza uma requisição GET na URL e guarda o resultado em uma variável
    response = requests.get(url)

    # Extrai o JSON da resposta da requisição
    result = response.json()

    # Respostas
    ultima = result[0]
    penultima = result[1]

    proxima_corrida = ultima['data_corrida']
    proxima_hora = ultima['prox_hora']
    proxima_minuto = ultima['minutos']
    vencedor_penultima = penultima['vencedor']
    vencedor_ultima = ultima['vencedor']
    tricast_ultima = ultima['tricast']
    tricast_penultima = penultima['tricast']


    #print('Vamos verificar se ',vencedor_ultima, ' estar na tricast ', tricast_penultima)
    if vencedor_ultima in tricast_penultima:
        entrada = numeros(tricast_ultima)
        separador = ', '
        minha_string = separador.join(entrada)
        #print('sim, ', vencedor_ultima, 'esta em', tricast_penultima, ', vamos entrar oposto ', entrada, 'as', proxima_hora)
    else:
        minha_string = tricast_ultima.replace("-", ",")
        #print('não, ', vencedor_ultima, 'não esta em', tricast_penultima, ', vamos entrar igual ', entrada, 'as', proxima_hora)

    retorno = {
        "entrada"   : str(entrada),
        "proxima_hora"    : proxima_hora
    }

    return jsonify(retorno)





if __name__ == "__main__":
    app.run()
