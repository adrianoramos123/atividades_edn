"""
4 - Crie um programa que calcule a quantos dias um individuo está vivo de acordo com a data do dia.
"""
from datetime import date

dia = int(input("Dia de nascimento: "))
mes = int(input("Mês de nascimento: "))
ano = int(input("Ano de nascimento: "))

data_nascimento = date(ano, mes, dia)
data_hoje = date.today()
diferenca_data = data_hoje - data_nascimento

print(f"Dias de vida até agora: {diferenca_data.days}")