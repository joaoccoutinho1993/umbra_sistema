# estoque = [
#    {"produto": "Chassis Titânio", "preco": 1000.00, "qtd": 2},
#    {"produto": "Cabo Nogueira",   "preco": 200.00,  "qtd": 5},
#    {"produto": "Neon Shell",      "preco": 300.00,  "qtd": 1}
# ]
def caclular_valor_total_estoque(estoque):
    valor_total_estoque = 0

    for item in estoque:
        itens = item["preco"] * item["qtd"]
        valor_total_estoque = valor_total_estoque + itens
    return valor_total_estoque


print(f"O valor total do armazém é R${caclular_valor_total_estoque:.2f}")
