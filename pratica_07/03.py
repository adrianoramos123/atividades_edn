"""
 3- Desenvolva um programa que cria um dicionário com dados de uma pessoa e salva esses dados em um arquivo JSON.
Em seguida, o programa deve ler o mesmo arquivo e exibir o conteúdo.
Para isso:

 * Crie um dicionário com pelo menos três campos (ex: nome, idade, cidade).
 * Solicite ao usuário o nome do arquivo JSON.
 * Salve os dados no arquivo usando o módulo `json`.
 * Após salvar, leia o mesmo arquivo e imprima os dados carregados.
 * Trate possíveis erros como ausência do arquivo ou problemas na escrita.

 Dica: Use `json.dump()` para escrever e `json.load()` para ler o arquivo.
"""
import json

dados_pessoas = [
    {"nome": "Ana", "idade": 20, "cidade": "Belo Horizonte"},
    {"nome": "Pedro", "idade": 30, "cidade": "Diamantina"},
    {"nome": "Maria", "idade": 23, "cidade": "Contagem"}
]

try:
    file = input("Digite o nome do arquivo: ") + ".json"

    with open(file, "w", encoding="utf-8") as f1:
        dados = json.dump(dados_pessoas, f1, indent=4, ensure_ascii=False)
    
    with open(file, "r", encoding="utf-8") as f2:
        print(json.load(f2))

except FileNotFoundError:
    print("Diretório/Arquivo não encontrado")
except PermissionError:
    print("Sem permissão para ler o arquivo")
except UnicodeEncodeError:
    print("Erro de codificação de caractere")
except OSError as e:
    print(f"Erro do sistema operacional: {e}")