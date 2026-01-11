"""
1- Conversor de Moeda
Crie um programa que converte um valor em reais para dólares e euros. Use os seguintes dados:

* Valor em reais: R$ 100.00
* Taxa do dólar: R$ 5.20
* Taxa do euro: R$ 6.15
O programa deve calcular e exibir os valores convertidos, arredondando para duas casas decimais.
"""

reais = 100.00
taxa_dolar = 5.20
taxa_euro = 6.15

print(f"R$ {reais: .2f} = $ {taxa_dolar*reais: .2f}")
print(f"R$ {reais: .2f} = € {taxa_euro*reais: .2f}")
