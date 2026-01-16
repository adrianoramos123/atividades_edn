"""
4 - Criar um código que serve para analisar números digitados pelo usuário,
classificando-os como pares ou ímpares e contabilizando quantos de cada tipo foram inseridos.
"""

impar = 0
par = 0
num = ""
while num != "fim":
    try:
        num = input("Digite um número: ")
        numero = int(num)
        if numero%2 == 0:
            par += 1
        else:
            impar += 1
    except ValueError:
        print("Valor inválido!")
        continue

print(f"Quantidade de números ímpares: {impar}")
print(f"Quantidade de números pares: {par}")