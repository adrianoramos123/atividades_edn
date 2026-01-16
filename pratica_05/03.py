"""
3 - Crie um programa que serve para calcular o preço final de um produto após aplicar um desconto percentual.
    a - Cálculo de desconto: Calcula o valor do desconto baseado em uma porcentagem.
    b - Preço final: Determina o novo preço após o desconto.
    c - Formatação: Arredonda o resultado para 2 casas decimais (centavos).
    d - Interação com usuário: Pede os valores necessários e mostra o resultado formatado.
"""

def calc_desconto(valor_atual, percentual_desconto):
    preco_final = valor_atual - (valor_atual*(percentual_desconto/100))
    return preco_final

valor_atual = float(input("Valor atual do produto (R$): "))
percentual_desconto = float(input("Percentual de desconto (%): "))

print(f"Preço final: R$ {calc_desconto(valor_atual, percentual_desconto): .2f}")