relatorio_velho = [
    "Cabo de Titânio | 250.00",
    "Tecido Kevlar | 120.50",
    "Neon RGB | 45.00",
]

estoque_limpo = []  # 1. Criamos a lista vazia (O "Galpão" novo)

print("--- Começando a Faxina ---")

for linha in relatorio_velho:
    # 2. O FACÃO: Quebramos a linha onde tem a barra "|"
    # A variável 'pedacos' vira uma lista temporária.
    # Ex: ['Cabo de Titânio ', ' 250.00']
    pedacos = linha.split("|")

    # 3. A LIMPEZA FINA:
    nome_sujo = pedacos[0]  # Pega a primeira parte
    preco_sujo = pedacos[1]  # Pega a segunda parte

    # 4. A TRANSFORMAÇÃO EM DICIONÁRIO (O que você pediu!)
    # Aqui a gente cria o objeto {chave: valor}
    produto_novo = {
        "produto": nome_sujo.strip(),  # Tira os espaços do nome
        "preco": float(preco_sujo.strip()),  # Tira espaços E converte pra número
    }

    # 5. O ARMAZENAMENTO
    # Joga o dicionário pronto dentro da lista principal
    estoque_limpo.append(produto_novo)

print("\n--- Resultado Final (JSON Bonitão) ---")
print(estoque_limpo)
