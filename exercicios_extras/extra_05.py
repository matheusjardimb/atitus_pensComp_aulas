"""
5- Conversor de reais para dólares.
Solicite ao usuário um valor (ex 500) e uma taxa de conversão (5,20).
Imprima na tela a conversão de reais para dólares (96.15 usd)
"""

valor = float(input("Digite um valor em reais: R$ "))
dolar = float(input("Digite quantos reais valem 1 dolar: R$ "))

convertido = valor / dolar
print(f"Seus R$ {valor} valem $ {convertido}")
