from typing import List, Dict
from flask import Flask, request, jsonify, render_template, redirect, flash, jsonify, abort
import mysql.connector
import json
import requests

from classes.cls_db import cls_dbAktionen

app = Flask(__name__)
app.config["DEBUG"] = True
app.config['SECRET_KEY'] = 'you-will-never-guess'





@app.route('/', methods=['GET'])
def home():
    return "<h1>Demoanwendung</h1>" \
           "<h3>Komponente Regelengine (eigener Entwicklungsstrang)</h3>"


# Teil, der in den Service wandern muss
@app.route('/api/v1/resources/verifyKunde', methods=['GET', 'POST'])
def api_verify():
    if not request.json:
        abort(502, "Format ungültig (Auftrag sieht irgendwie doof aus!)")

    print("request: ", request.json)
    dictKunde = {
        'kunde': request.json
    }
    status = verifyKunde(dictKunde)
    print("Status aus api_verify: ", status)
    return jsonify({'status': status}), 200


def verifyKunde(dictKunde):
    print(dictKunde)
    status = {}

    # Prüfung Rolle
    if not dictKunde['kunde']['rolle'].isnumeric():
        status['result'] = 'nok'
        status['rc'] = 'Ungültiger Wert in Feld \'Rolle\''

    # Prüfung Anrede
    if not dictKunde['kunde']['anrede'].isnumeric():
        status['result'] = 'nok'
        status['rc'] = 'Ungültiger Wert in Feld \'Anrede\''

    # Prüfung PANR
    if not dictKunde['kunde']['plz'].isnumeric():
        status['result'] = 'nok'
        status['rc'] = 'PLZ nicht numerisch'




    if not status:
        status['result'] = 'ok'
        status['rc'] = 'Prüfungen erfolgreich'

    print(status)

    return status

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5010')