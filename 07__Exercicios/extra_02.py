"""
2 - Crie uma lista manualmente com 10 números fora de ordem e imprima na tela:
"""

lista = [5, 2, 6, -8, 7, 3, 5, 1, 6, 90]

# - Qual o maior número da lista.
# Assumimos que o primeiro valor é o maior. Se não for, será atualizado no for
maior = lista[0]
for valor in lista:
    if valor > maior:
        maior = valor
print("Qual o maior número da lista?", maior)

# - Qual o menor número da lista.
# Assumimos que o primeiro valor é o menor. Se não for, será atualizado no for.
menor = lista[0]
for valor in lista:
    if valor < menor:
        menor = valor
print("Qual o menor número da lista?", menor)

# - Quais números são pares.
pares = []
for valor in lista:
    if valor % 2 == 0:
        pares.append(valor)
print("Quais números são pares?", pares)

# - Quais números são ímpares.
ỉmpares = []
for valor in lista:
    if valor % 2 != 0:
        ỉmpares.append(valor)
print("Quais números são ỉmpares?", ỉmpares)

# - Quais números são positivos
positivos = []
for valor in lista:
    if valor > 0:
        positivos.append(valor)
print("Quais números são positivos?", positivos)

# - Quais números são negativos.
negativos = []
for valor in lista:
    if valor < 0:
        negativos.append(valor)
print("Quais números são negativos?", negativos)

# - A soma de todos os números.
soma_total = lista.pop()
for valor in lista:
    soma_total += valor
print("Soma total?", soma_total)
