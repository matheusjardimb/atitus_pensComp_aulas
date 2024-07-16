# Você está escrevendo o módulo de vendas para um PDV (Ponto De Venda) de caixa de supermercado.


def obtem_quantidade() -> int:
    quantidade = -1
    while quantidade < 0:
        # Solicite ao operador do caixa a quantidade de itens e o valor de cada item.
        quantidade = int(input("Digite a quantidade de itens:"))

    return quantidade


def obtem_valor() -> float:
    # Solicite ao operador do caixa a quantidade de itens e o valor de cada item.
    return float(input("Digite o valor de cada item:"))


valor_total = 0
while True:
    quantidade = obtem_quantidade()
    # Se o operador digitar 0 (zero) na quantidade de itens
    if quantidade == 0:
        # Encerre a venda calculando o total e exiba na tela.
        break

    valor = obtem_valor()
    sub_total = quantidade * valor
    valor_total = valor_total + sub_total
    print(f"Subtotal: {sub_total}")
    # A cada par de entrada (quantidade e valor) imprima o subtotal do mesmo.

print(f"Total: {valor_total}")

# Organize o código em funções e tipifique os parâmetros de entrada e saída.
