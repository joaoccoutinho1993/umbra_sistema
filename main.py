import analise
import logistica

estoque = [
    {"produto": "Chassis Titânio", "preco": 1000.00, "qtd": 2},
    {"produto": "Cabo Nogueira", "preco": 200.00, "qtd": 5},
    {"produto": "Neon Shell", "preco": 300.00, "qtd": 1},
]

print(f"O total do preço do estoque deu {analise.calcular_total(estoque):.2f}")

regiao = input("Qual é a região para envio? ")

print(f"O valor total do frete é R${logistica.calcular_frete(regiao):.2f}")

while True:
    try:
        desconto = int(input("Digite o desconto: "))

        if 0 <= desconto <= 100:
            print(f"Sucesso, desconto de {desconto}% aplicado!")
            break
        else:
            print("Erro, desconto precisa ser um número de 0 a 100%")

    except ValueError:
        print("Erro! Use apenas números!")

# O programa continua vivinho aqui em baixo!
print("Fim do programa.")
