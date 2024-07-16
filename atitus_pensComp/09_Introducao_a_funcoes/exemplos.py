def soma(a, b):
    return a + b


def subtracao(a, b):
    return a - b


def multiplicacao(a, b):
    return a * b


a = int(input("Digite o numero"))
b = int(input("Digite o numero"))

print(multiplicacao(soma(a, b), subtracao(a, b)))
