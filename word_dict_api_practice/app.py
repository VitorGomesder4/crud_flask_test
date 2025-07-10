from flask import Flask, request, jsonify
from models.palavra import Palavra

#API de Dicionário de Palavras

#Endpoints:

#    GET /words: Lista todas as palavras.

#    GET /words/<word>: Retorna o significado.

#    POST /words: Adiciona uma nova palavra.

#    PUT /words/<word>: Atualiza o significado.

#    DELETE /words/<word>: Remove a palavra.

# Pratica: CRUD completo com dicionários Python.

app = Flask(__name__)

lista_palavras = []

@app.route("/words", methods=['POST'])
def post_word():
    data = request.get_json()

    if data.get("palavra").strip() == "" or data.get("significado").strip() == "":
        return jsonify({"message": "informação incompleta"}), 400

    if lista_palavras:
        for p in lista_palavras:
            if data.get("palavra") == p.palavra:
                return jsonify({"message": f"palavra '{p.palavra}' ja esta no dicionario"}), 400

    palavra = Palavra(palavra = data.get("palavra"), significado = data.get("significado"))
    lista_palavras.append(palavra)

    return jsonify({"message": "palavra adicionada ao dicionario"}), 200


@app.route("/words", methods=['GET'])
def get_words():
    if lista_palavras:
        return jsonify([p.to_dict() for p in lista_palavras]), 200
    return jsonify({"message": "dicionario vazio"}), 400


@app.route("/words/<word>", methods=['GET'])
def get_word(word):
    if lista_palavras:
        for p in lista_palavras:
            if word == p.palavra:
                return jsonify(p.to_dict()), 200
        return jsonify({"message": f"palavra '{word}' não se encontra no dicionario"}), 404

    return jsonify({"message": "dicionario não possui palavras"}), 400


@app.route("/words/<word>", methods=['PUT'])
def put_word(word):
    data = request.get_json()

    if lista_palavras:
        for p in lista_palavras:
            if p.palavra == word:
                p.palavra = data.get("palavra")
                p.significado = data.get("significado")
                return jsonify({"message": f"palavra '{word}' atualizada com sucesso"}), 200

        return jsonify({"message": "palavra não se encontra no dicionario"}), 404

    return jsonify({"message": "dicionario não possui palavras"}), 400

@app.route("/words/<word>", methods=['DELETE'])
def delete_word(word):

    if lista_palavras:
        for p in lista_palavras:
            if p.palavra == word:
                lista_palavras.remove(p)
                return jsonify({"message": f"palavra '{word}' removida com sucesso"}), 200
        return jsonify({"message": f"palavra '{word}' não se encontra no dicionario"}), 404

    return jsonify({"message": "dicionario não possui palavras"}), 400

if __name__ == "__main__":
    app.run(debug=True)