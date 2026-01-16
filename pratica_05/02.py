"""
2 - Crie uma função que verifique se uma palavra ou frase é um palíndromo
(lê-se igual de trás para frente, ignorando espaços e pontuação).
Se o resultado é True, responda “Sim”, se o resultado for False, responda “Não”.
"""
import unicodedata # Permite remover pontuação, espaços e normaliza acentos.

def remove_pontuacao(palavra):
    palavra_sem_acentos = ''.join(
        c for c in unicodedata.normalize('NFD', palavra)
        if unicodedata.category(c) != 'Mn'
    )
    # Mantém apenas letras e números
    palavra_limpa = ''.join(c for c in palavra_sem_acentos if c.isalnum())
    return palavra_limpa.lower()


palavra = input("Digite uma palavra ou frase: ")
palavra_sem_pontuacao = remove_pontuacao(palavra)
palavra_inversa = palavra_sem_pontuacao[::-1]

if palavra_inversa == palavra_sem_pontuacao:
    print("Sim")
else:
    print("Não")
