A = int(input("digite a: "))
B = int(input("digite b: "))
C = int(input("digite c: "))
delta = B**2 - 4 * A * C
div = 2 * A
x1 = (-B - delta ** (1 / 2)) / div
x2 = (-B + delta ** (1 / 2)) / div
print("os valores das raízes de x são: ", x1, " e ", x2, ".")
