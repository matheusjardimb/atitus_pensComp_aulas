"""
10 - Solicite uma temperatura ao usuário e imprima e assuma que:
- o valor digitado estava em Fahrenheit e imprima o valor convertido para Celsius
- o valor digitado estava em Celsius e imprima o valor convertido para Fahrenheit
"""

temperatura = float(input("Digite a temperatura: "))
fahrenheit = (temperatura * 9 / 5) + 32
celsius = (temperatura - 32) * 5 / 9
print(f"A temperatura {temperatura} em fahrenheit é {fahrenheit}")
print(f"A temperatura {temperatura} em celsius é {celsius}")
