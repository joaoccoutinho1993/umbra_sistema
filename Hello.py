"""
Exercício 3.6: Escreva uma expressão que será utilizada para decidir se um aluno ou não foi aprovador.
Para ser aprovado, todas as médias do aluno devem ser maiores ou iguais a 7. Considere que o aluno cursa apenas três matérias,
e que a nota de cada uma está armazenada ans seguintes variáveis: materia1, materia2 e materia3.
"""

materia1 = float(input("Digite a nota da primeira materia: "))
materia2 = float(input("Digite a nota da segunda materia: "))
materia3 = float(input("Digite a nota da terceira materia:"))

if materia1 and materia2 and materia3 >= 7:
    print("Parabéns, você foi aprovado!")
else:
    print("Você foi reprovado.")
