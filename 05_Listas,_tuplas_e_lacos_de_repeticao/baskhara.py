def baskhara(a, b, c):
    pass


A = 2
B = 3
C = -2
# [-2, 0.5]

A = 1
B = -5
C = 6

# [2, 3]

delta = B**2 - 4 * A * C
div = 2 * A
x1 = (-B - delta ** (1 / 2)) / div
x2 = (-B + delta ** (1 / 2)) / div
print("os valores das raízes de x são: ", x1, " e ", x2, ".")
