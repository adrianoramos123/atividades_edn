"""
3 - Crie um programa que consulte informações de um CEP na API ViaCEP, retorne logradouro,
bairro, cidade e estado do CEP digitado, caso o CEP não existir ou houver erro na requisição,
mostre uma mensagem de falha.
"""
import requests

cep = input("Digite o CEP: ")
url = f"https://viacep.com.br/ws/{cep}/json/"
resp = requests.get(url)

if resp.status_code == 200:
    data = resp.json()
    if "erro" in data:
        print("Erro: CEP inválido!")
    else:
        print(f"Logradouro: {data["logradouro"]}")
        print(f"Bairro: {data["bairro"]}")
        print(f"Cidade: {data["localidade"]}")
        print(f"Estado: {data["estado"]}")

elif resp.status_code == 400:
    print("Erro: formato de CEP inválido!")
else:
    print("Erro: falha na conexão!")
