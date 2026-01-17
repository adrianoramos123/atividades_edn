"""
4 - Crie um programa que realize consultas a cotações de moedas em relação ao Real (BRL) usando a API AwesomeAPI,
 mostre valor atual, máxima, mínima e data/hora da última atualização, caso a moeda não existir ou houver erro na
 requisição, retorne uma mensagem de erro.  
"""
import requests

try:
    print("Escolha uma opção de cotação de moedas em relação ao Real (BRL): ")
    print("1. USD-BRL (Dólar Americano/Real Brasileiro)")
    print("2. EUR-BRL (Euro/Real Brasileiro)")
    print("3. BTC-BRL (Bitcoin/Real Brasileiro)")
    
    moedas = ["USD-BRL", "EUR-BRL", "BTC-BRL"]
    opcao = int(input("Digite a opção de cotação que deseja visualizar: "))

    if opcao > 0 and opcao < 4:
        url = f"https://economia.awesomeapi.com.br/json/last/{moedas[opcao-1]}"
        resp = requests.get(url)

        if resp.status_code == 200:
            key = moedas[opcao-1].replace("-", "")
            data = resp.json()
            print()
            print("****"*15)
            print(f"{data[key]["name"]}")
            print(f"Valor atual: {data[key]["bid"]}")
            print(f"Máxima: {data[key]["high"]}")
            print(f"Mínima: {data[key]["low"]}")
            print(f"Data/hora da última atualização: {data[key]["create_date"]}")
            print("****"*15)
        elif resp.status_code == 404:
            print("Moeda não encontrada ABC-BRL")
        else:
            print("Falha na conexão!")
    else:
        print("Opção inválida!")
except ValueError:
    print("Valor inválido!")