# Arquivo: app.py

# 1. IMPORTANDO (Pegando as coisas dos outros arquivos)
from aluno import Aluno  # Do arquivo aluno, traga o cortador Aluno
import utils  # Traga a caixa de ferramentas inteira

while True:
    print("\n--- SISTEMA SENAC ---")

    # 2. ENTRADA DE DADOS (Você já sabe isso)
    nome = input("Digite o nome do aluno: ")
    n1 = float(input("Digite a nota 1: "))
    n2 = float(input("Digite a nota 2: "))
    lista_de_notas = [n1, n2]

    # 3. CRIANDO O OBJETO (Usando o Cortador de Biscoito)
    # Criamos uma variável 'aluno_atual' que é um Objeto real
    aluno_atual = Aluno(nome, lista_de_notas)

    # 4. USANDO AS FERRAMENTAS (Utils)
    # Note: Passamos 'aluno_atual.notas' (as notas que estão dentro do objeto)
    media_final = utils.calcular_media(aluno_atual.notas)
    status = utils.verificar_situacao(media_final)

    # 5. MOSTRANDO O RESULTADO
    # Acessamos o nome que está guardado dentro do objeto (aluno_atual.nome)
    print(f"O aluno {aluno_atual.nome} teve média {media_final:.1f}")
    print(f"Situação: {status}")

    # Sair do loop
    sair = input("Deseja cadastrar outro? (S/N): ")
    if sair.upper() == "N":
        break

print("Sistema Encerrado.")
