from flask import Flask, request, jsonify
import json

app = Flask(__name__)
localizacoes = []

def salvar_localizacoes():
    with open('localizacoes.json', 'w') as file:
        json.dump(localizacoes, file)

def carregar_localizacoes():
    global localizacoes
    try:
        with open('localizacoes.json', 'r') as file:
            localizacoes = json.load(file)
    except FileNotFoundError:
        localizacoes = []

@app.route('/api/localizacao', methods=['POST'])
def receber_localizacao():
    localizacao = request.get_json()
    print("Localização recebida:", localizacao)

    localizacoes.append(localizacao)
    salvar_localizacoes()

    resposta = {'message': 'Localização recebida com sucesso'}
    return jsonify(resposta)

@app.route('/api/localizacao', methods=['GET'])
def obter_localizacao():
    if not localizacoes:
        resposta = {'message': 'Nenhuma localização disponível'}
    else:
        ultima_localizacao = localizacoes[-1]
        resposta = ultima_localizacao

    return jsonify(resposta)

if __name__ == '__main__':
    carregar_localizacoes()
    app.run(host='0.0.0.0', port=5000)
