import pandas as pd
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def inicial():
    return 'API no ar'

@app.route('/speedway')
def speedway():
    teste = {"nome": "ezequiel"}
    return jsonify(teste)


app.run(host='0.0.0.0', debug=True)