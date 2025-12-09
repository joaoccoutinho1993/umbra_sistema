def calcular_frete(regiao: str) -> float:
    regiao_limpa = regiao.strip().lower()
    if regiao_limpa == "sudeste":
        return 20.00
    elif regiao_limpa == "sul":
        return 30.00
    else:
        return 50.00


print(calcular_frete(""))
