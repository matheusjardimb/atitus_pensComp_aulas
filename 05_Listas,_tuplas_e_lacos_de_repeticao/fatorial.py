number = int(input("Digite um número para calcular a sua fatorial:"))
fatorial = 1
for x in range(number):
    fatorial = fatorial * (x + 1)
print("Fatorial de ", number, "é", fatorial)
