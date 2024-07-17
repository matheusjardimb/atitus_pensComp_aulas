"""
9 - Solicite o valor de um produto e a forma de pagamento (um número, referente à lista abaixo):
Tabela de Código de Condições de Pagamento
"""

valor_produto = float(input("Digite o valor do produto: "))

print("Formas de pagamento:")
print("1 - À Vista em Dinheiro ou Pix, recebe 15% de desconto")
print("2 - À Vista no cartão de crédito, recebe 10% de desconto")
print("3 - Parcelado no cartão em duas vezes, preço normal do produto sem juros")
print(
    "4 - Parcelado no cartão em três vezes ou mais, preço normal do produto mais juros de 10%"
)

forma_pgto = int(input("Digite a forma de pagamento: "))
match forma_pgto:
    case 1:
        juros = 0.85
    case 2:
        juros = 0.90
    case 3:
        juros = 1
    case _:
        juros = 1.1

print(f"Valor pago: {valor_produto * juros}")
