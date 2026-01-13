"""
4- Verificador de Ano Bissexto
Faça um programa que determine se um ano inserido pelo usuário é bissexto ou não.
Um ano é bissexto se for divisível por 4, exceto anos centenários (divisíveis por 100) que não são divisíveis por 400.
"""

ano = int(input("Informe o ano: "))

if ano%4 == 0:
    if ano%100 == 0 and ano%400 != 0:
        print("Não é bissexto")
    else:
        print("É bissexto")
else:
    print("Não é bissexto")