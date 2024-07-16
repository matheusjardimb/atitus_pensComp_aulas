"""
8- Solicite 4 notas obtidas por um aluno e imprima a média das nota
média = (a+b+c+d) / 4
Imprima se o aluno foi aprovado (média >= 7) ou não.
"""

NUM_NOTAS = 4
soma_notas = 0
for i in range(NUM_NOTAS):
    soma_notas += int(input(f"Digite a nota {i + 1}: "))

media = soma_notas / NUM_NOTAS
print(f"A media é {media}")

if media >= 7:
    print("Aluno aprovado")
else:
    print("Aluno reprovado")
