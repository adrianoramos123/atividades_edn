"""
2- Desenvolva um programa que lê os dados de um arquivo CSV e imprime cada linha na tela.
Para isso:

 * Solicite ao usuário o nome do arquivo CSV a ser lido.
 * Utilize o módulo `csv` para abrir o arquivo e ler os dados.
 * Exiba cada linha completa como uma lista.
 * Trate erros como arquivo inexistente ou problemas na leitura.

 Dica: Use `csv.reader()` para ler e percorrer as linhas do arquivo.
"""
import csv

try:
    file = input("Digite o nome do arquivo a ser lido: ") + ".csv"
    with open(file, 'r', newline="", encoding="utf-8") as arquivo:
        rows = csv.reader(arquivo)
        for row in rows:
            print(row)

except FileNotFoundError:
    print("Diretório/Arquivo não encontrado")
except PermissionError:
    print("Sem permissão para ler o arquivo")
except UnicodeEncodeError:
    print("Erro de codificação de caractere")
except OSError as e:
    print(f"Erro do sistema operacional: {e}")