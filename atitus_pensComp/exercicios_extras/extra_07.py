"""
7- Calculadora IMC (Índice de Massa Corporal). Solicite ao usuáiro o peso e altura.
Imprima na tela o índice:
"""

altura = float(input("Digite a altura: "))
peso = float(input("Digite o peso: "))

# Fórmula do IMC = peso / (altura)²
imc = peso / altura**2
print(f"O IMC é {imc}")
if imc < 18.5:
    print("Nível 1: Abaixo de 18,5 | Abaixo do peso")
elif imc < 24.9:
    print("Nível 2: Entre 18,6 e 24,9 | Peso ideal")
elif imc < 29.9:
    print("Nível 3: Entre 25,0 e 29,9 | Levemente acima do peso")
elif imc < 34.9:
    print("Nível 4: Entre 30,0 e 34,9 | Obesidade grau I")
elif imc < 39.9:
    print("Nível 5: Entre 35,0 e 39,9 | Obesidade grau II (severa)")
else:
    print("6- Maior ou igual a 40 | Obesidade grau III (mórbida)")
