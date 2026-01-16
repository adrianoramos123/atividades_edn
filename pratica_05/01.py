"""
1 - Crie uma função que calcule a gorjeta a ser deixada em um restaurante, baseada no valor total da conta e na porcentagem de
gorjeta desejada. Calcula o valor da gorjeta baseado no total da conta e na porcentagem desejada.
Parâmetros:
    a - valor_conta (float): O valor total da conta
    b - porcentagem_gorjeta (float): A porcentagem da gorjeta (ex: 10 para 10%)
    c - retorna: float: O valor da gorjeta calculada
"""

def gorjeta(valor, porcentagem_gorjeta):
    valor_gorjeta = valor * (porcentagem_gorjeta/100)
    return valor_gorjeta

def entrada_info(descricao):
    while True:
        try:
            valor = float(input(f"Digite o valor {descricao}: "))
            return valor
        except ValueError:
            continue

valor_conta = entrada_info("total da conta R$")
porcentagem_gorjeta = entrada_info("da porcentagem de gorjeta")

print(f"Valor da gorjeta (R$): {gorjeta(valor_conta, porcentagem_gorjeta): .2f}")