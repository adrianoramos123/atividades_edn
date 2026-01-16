"""
2 - Criar um código que registre as notas de alunos e calcular a média da turma.
"""
soma = 0
cont = 0
nota = ""
while nota != "fim":
    try:
        nota = input("Digite a nota: ")
        notas = float(nota)
        if notas >= 0 and notas <= 10:
            soma += notas
            cont += 1
    except ValueError:
        continue

print(f"Média de notas: {soma/cont: .2f}")