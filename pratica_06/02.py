"""
2 - Crie um programa que acesse a API Random User Generator para buscar um usuário fictício aleatório.
Exibindo o nome, e-mail e país desse usuário, caso houver erro na conexão, mostre uma mensagem de falha.
"""
import requests

url = "https://randomuser.me/api/"
resp = requests.get(url)

if resp.status_code == 200:
    data = resp.json()
    print(f"Nome: {data["results"][0]["name"]["first"]} {data["results"][0]["name"]["last"]}")
    print(f"E-mail: {data["results"][0]["email"]}")
    print(f"País: {data["results"][0]["location"]["country"]}")
else:
    print("Erro: falha na conexão!")