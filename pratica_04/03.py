"""
3 - Criar um código que serve para verificar se uma senha digitada pelo usuário atende a critérios básicos de segurança.
    a - deve ter pelo menos 8 caracteres.
    b - deve conter pelo menos um número.
"""

digitos="0123456789"
senha = ""
while senha != "sair":
    senha = input("Digite uma senha: ")
    if len(senha) >= 8:
        tem_digito = any(char.isdigit() for char in senha)
        if tem_digito:
            print("Senha forte")
            break
        else:
            print("Senha fraca")
            continue
    
    print("Senha fraca")
    continue