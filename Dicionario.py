pedido_umbra = {
    "cliente": "Motoko",
    "itens": [
        {"produto": "Chassis Titânio", "preco": 1200.00},
        {"produto": "Shell Neon", "preco": 350.00}
    ],
    "total": 1550.00
}

seguro = {"produto": "Seguro Chuva Ácida", "preco": 75.00}

pedido_umbra["itens"].append(seguro)


pedido_umbra["total"] = sum(item["preco"] for item in pedido_umbra["itens"])

print(pedido_umbra)
