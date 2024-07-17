def soma_pares(numeros: list, alvo: int) -> bool:
    for x in numeros:
        for y in numeros:
            if x + y == alvo:  # and x != y
                print(f"Considerando {numeros}, {x} + {y} = {alvo}")
                return True
    return False


print(soma_pares([1, 2], 4))  # True
print(soma_pares([8], 1))  # False
print(soma_pares([8], 10))  # False
print(soma_pares([3, 4, 6], 9))  # True
print(soma_pares([3, 4, 6], 7))  # True
