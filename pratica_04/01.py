"""
1 - Criar um código que faça uma calculadora que tenha as operações básicas(+,-,*,/).
"""

def number(ordem, operador=None):
    while True:
        try:
            num = float(input(f"Digite o {ordem}º número: "))
            
            if operador == '/' and num == 0:
                print("Erro: divisão por zero não é permitida!")
                continue
            return num

        except ValueError:
            print("Erro: valor inválido")

def menu_operacoes():
    print("Operações válidas")
    print("+ (adição)")
    print("- (subtração)")
    print("* (multiplicação)")
    print("/ (divisão)")

def choice_operator():
    operadores = ['+', '-', '*', '/']
    
    while True:
        menu_operacoes()
        operador = input("Digite a operação: ")
        if operador in operadores:
            return operador
        else:
            print("Operador arimético inválido!")
            print("Digite um operador válido!")


num1 = number(1)
operador = choice_operator()
num2 = number(2, operador)
expressao = f"{num1}{operador}{num2}"
print(f"\n{expressao} = {eval(expressao)}")