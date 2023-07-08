import requests

API_URL = 'http://localhost:5000/api/localizacao'

def obter_localizacao_servidor():
    response = requests.get(API_URL)
    if response.status_code == 200:
        localizacao = response.json()
        print("Localização recebida:", localizacao)
    else:
        print("Falha ao obter localização do servidor.")

if __name__ == '__main__':
    obter_localizacao_servidor()
