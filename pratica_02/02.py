"""
2- Calculadora de Desconto
Desenvolva um programa que calcula o desconto em uma loja. Use as seguintes informações:

* Nome do produto: "Camiseta"
* Preço original: R$ 50.00
* Porcentagem de desconto: 20%
O programa deve calcular o valor do desconto e o preço final, exibindo todos os detalhes.
"""

preco_original = 50.00
porcentagem = 0.2
valor_desconto = preco_original*porcentagem
preco_final = preco_original - valor_desconto

print("Nome do produto: Camiseta")
print(f"Preço original: R$ {preco_original}")
print(f"Porcentagem de desconto: {porcentagem}%")
print(f"Valor do desconto: R$ {valor_desconto: .2f}")
print(f"Preço final: R$ {preco_final: .2f}")