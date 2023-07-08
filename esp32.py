import requests
import json

# URL da API
url = 'http://localhost:5000/api/localizacao'

# Dados da localização
localizacao = {
    'latitude': 12.345,
    'longitude': -67.89
}

# Definir o cabeçalho Content-Type como application/json
headers = {'Content-Type': 'application/json'}

# Converter o dicionário para JSON
json_data = json.dumps(localizacao)

# Enviar a requisição POST para a API
response = requests.post(url, data=json_data, headers=headers)

# Verificar a resposta do servidor
if response.status_code == 200:
    # Requisição bem-sucedida
    print('Localização enviada com sucesso!')
else:
    # Erro na requisição
    print('Erro ao enviar localização:', response.status_code)
    print('Mensagem de erro:', response.text)
