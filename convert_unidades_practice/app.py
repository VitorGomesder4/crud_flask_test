from flask import Flask, request, jsonify

from models.temperatura import Temperatura
from models.comprimento import Comprimento
from models.peso import Peso

app = Flask(__name__)

ultima_temperatura = None
ultimo_comprimento = None
ultimo_peso = None

#TEMPERATURA
@app.route('/temperatura', methods=['POST'])
def converter_temperatura():
    global ultima_temperatura
    data = request.get_json()
    ultima_temperatura = Temperatura(tipo=data.get("tipo"), quantidade=data.get("quantidade"))
    ultima_temperatura.converter()
    return jsonify({"message": "sucesso"}), 200

@app.route('/temperatura', methods=['GET'])
def get_temperatura():
    if not ultima_temperatura:
        return jsonify({"message": "Nenhuma temperatura convertida"}), 404
    else:
        return jsonify({"celsius": ultima_temperatura.cel, "fahrenheit": ultima_temperatura.fahr}), 200

#COMPRIMENTO
@app.route('/comprimento', methods=['POST'])
def converter_comprimento():
    global ultimo_comprimento
    data = request.get_json()
    ultimo_comprimento = Comprimento(tipo=data.get("tipo"), quantidade=data.get("quantidade"))
    ultimo_comprimento.converter()
    return jsonify({"message": "sucesso"}), 200

@app.route('/comprimento', methods=['GET'])
def get_comprimento():
    if not ultimo_comprimento:
        return jsonify({"message": "Nenhum comprimento convertido"}), 404
    else:
        return jsonify({"metros": ultimo_comprimento.metros, "pes": ultimo_comprimento.pes}), 200

#PESO
@app.route('/peso', methods=['POST'])
def converter_peso():
    global ultimo_peso
    data = request.get_json()
    ultimo_peso = Peso(tipo=data.get("tipo"), quantidade=data.get("quantidade"))
    ultimo_peso.converter()
    return jsonify({"message": "sucesso"}), 200

@app.route('/peso', methods=['GET'])
def get_peso():
    if not ultimo_peso:
        return jsonify({"message": "Nenhum peso convertido"}), 404
    else:
        return jsonify({"KG": ultimo_peso.kg, "LB": ultimo_peso.lb}), 200

if __name__ == "__main__":
    app.run(debug=True)