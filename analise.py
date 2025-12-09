# Arquivo: analise.py

def calcular_total(lista_generica):
    total = 0
    for item in lista_generica:
        # Note que a gente confia que quem chamar vai mandar 
        # uma lista de dicionários com "preco" e "qtd"
        subtotal = item["preco"] * item["qtd"]
        total = total + subtotal
    
    return total