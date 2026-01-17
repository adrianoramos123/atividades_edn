"""
1 - Crie um programa que gere senhas aleatórias com letras, números e símbolos e que o usuário
  também escolha o tamanho da senha  para criar senhas seguras automaticamente.
"""
import requests

url = "https://api.genratr.com/"
size = int(input("Digite o tamanho da senha: "))

params = {
    "length": size,
    "uppercase": True,
    "lowercase": True,
    "special": True,
    "numbers": True
}

resp = requests.get(url, params=params)

if resp.status_code == 200:
    dados = resp.json()
    senha = dados["password"]
    print(f"Senha gerada: {senha}")
else:
    print("Erro ao gerar senha")