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
    teste = {"nome": tempo}
    return jsonify(teste)

if __name__ == "__main__":
    app.run()
