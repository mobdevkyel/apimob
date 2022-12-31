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


if __name__ == "__main__":
    app.run(debug=True)
