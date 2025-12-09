# Arquivo: analise.py


def calcular_total(lista_generica: list) -> float:
    """
    Calcula o valor total do estoque baseado no preço e quantidade.

    Args:
        lista_de_produtos (list): Lista de dicionários contendo 'preco' e 'qtd'.

    Returns:
        float: O valor total somado de todos os itens.
    """
    total = 0
    for item in lista_generica:
        subtotal = item["preco"] * item["qtd"]
        total = total + subtotal

    return total
