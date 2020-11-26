from flask import Flask
from table import Table
from grupo_familiar import GrupoFamiliar
from levantamiento import Levantamiento
from flask import jsonify

app = Flask(__name__)


@app.route('/')
def index():
    return "is working!!"


@app.route('/requerimientos')
def requerimientos():

    return 'requerimientos'


@app.route('/familiar')
def familiar():
    grupo_familiar = GrupoFamiliar()
    return jsonify(grupo_familiar.totales())


@app.route('/levantamiento')
def levantamiento():
    levantamiento = Levantamiento()
    return levantamiento.totales()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
