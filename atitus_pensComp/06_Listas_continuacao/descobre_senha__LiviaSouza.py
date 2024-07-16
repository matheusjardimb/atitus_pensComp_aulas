# import random
# numero_secreto = random.randint(1, 10)

print("Bem-vindo ao Jogo!")

numero_secreto = 5

tentativas = 0
max_tentativas = 5

while tentativas < max_tentativas:
    palpite = int(input("Tente adivinhar o número: "))

    if palpite == numero_secreto:
        print("Parabéns! Você acertou!")
        break
    elif palpite > numero_secreto:
        print("Tente um número menor.")
    else:
        print("Tente um número maior.")

    tentativas += 1

if tentativas == max_tentativas:
    print("Fim do jogo.")
