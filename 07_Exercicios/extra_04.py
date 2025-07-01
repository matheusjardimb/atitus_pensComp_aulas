# 6- Solicite três números (x,y,z) ao usuário e:
# Retorne x caso (y * z) for maior que x
# Retorne y caso (x + y) for maior que z
# Retorne z caso (z - y) for maior que x
# Do contrário, retorne (x + y + z)


def operacao(x, y, z):
    if (y * z) > x:
        return x
    if (x + y) > z:
        return y
    if (z - y) > x:
        return z
    return x + y + z


x = int(input("Digite um valor: "))
y = int(input("Digite um valor: "))
z = int(input("Digite um valor: "))
print(operacao(x, y, z))
