# --- DESAFIO 1: A Calculadora de Média (*args) ---
# Objetivo: A função deve receber N notas e retornar a média delas.

def calcular_media(*notas):
    print(f"Calculando média de {len(notas)} notas...")
    
    # DICA: Você precisa somar todas as notas e dividir pela quantidade.
    # notas é uma tupla: (10, 8, 9...)
    
    # 1. Crie uma variável para soma
    soma = 0
    
    # 2. Faça um loop for nas notas para somar (SEU CÓDIGO AQUI)
    for nota in notas:
        soma += nota
    
    # 3. Calcule a média (soma / quantidade) (SEU CÓDIGO AQUI)
    media = soma/len(notas) # Substitua pelo cálculo
    
    return media

# Teste do Desafio 1
print(f"Média do Aluno 1: {calcular_media(10, 8, 9)}") # Deve dar 9.0
print(f"Média do Aluno 2: {calcular_media(5, 5, 5, 5, 10)}") # Deve dar 6.0


print("\n" + "="*30 + "\n")


# --- DESAFIO 2: O Montador de PC (**kwargs) ---
# Objetivo: Mostrar as peças escolhidas pelo cliente.

def montar_pc(**pecas):
    print("--- Configuração do PC ---")
    
    # DICA: pecas é um dicionário: {'cpu': 'i5', 'ram': '8gb'}
    # Use um loop for com pecas.items() para pegar chave e valor
    
    # (SEU CÓDIGO AQUI: Faça um loop que printe "Peça: Modelo")
    pass 

# Teste do Desafio 2
montar_pc(cpu="Intel i7", ram="16GB", placa_video="RTX 3060")
montar_pc(cpu="Ryzen 5", armazenamento="SSD 1TB") # Note que os argumentos mudam!