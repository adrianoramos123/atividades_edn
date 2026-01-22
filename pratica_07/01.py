"""
1- Crie um programa que escreve dados de pessoas (nome, idade e cidade) em um arquivo CSV.
Para isso:

 * Crie uma lista de listas com dados fictícios de pelo menos três pessoas.
 * Solicite ao usuário o nome do arquivo CSV onde os dados serão salvos.
 * Escreva os dados usando o módulo `csv`, com cabeçalhos apropriados.
 * Confirme a gravação exibindo uma mensagem com o nome do arquivo.
 * Trate possíveis erros de escrita de arquivo.

 Dica: Use `csv.writer()` para escrever os dados linha por linha.
"""
import csv

pessoas = [
    ["Ana", 20, "Belo Horizonte"],
    ["Pedro", 30, "Diamantina"],
    ["Maria", 23, "Contagem"]
]

try:
    file = input("Digite o nome do arquivo: ") + ".csv"
    with open(file, 'w', newline="", encoding="utf-8") as arquivo:
        wr = csv.writer(arquivo)
        wr.writerow(["nome", "idade", "cidade"])
        wr.writerows(pessoas)
    print(f"Arquivo criado: {file}")
except FileNotFoundError:
    print("Diretório/Arquivo não encontrado")
except PermissionError:
    print("Sem permissão para escrever o arquivo")
except UnicodeEncodeError:
    print("Erro de codificação de caractere")
except OSError as e:
    print(f"Erro do sistema operacional: {e}")