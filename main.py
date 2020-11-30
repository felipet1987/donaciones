from flask import Flask

from requerimiento import Requerimiento
from grupo_familiar import GrupoFamiliar
from levantamiento import Levantamiento
from flask import jsonify

app = Flask(__name__)


@app.route('/')
def index():
    return "is working!!"

@app.route('/familiar')
def familiar():
    grupo_familiar = GrupoFamiliar()
    return jsonify(grupo_familiar.totales())

@app.route('/levantamiento')
def levantamiento():
    levantamiento = Levantamiento()
    return jsonify(levantamiento.totales())

@app.route('/requerimientos')
def requerimientos():
    requerimientos = Requerimiento()
    return jsonify(requerimientos.levantados())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
