def validador_parenteses(entrada: str) -> bool:
    conta_parenteses = 0
    for x in entrada:
        if x == "(":
            conta_parenteses += 1
        elif x == ")":
            conta_parenteses -= 1
        if conta_parenteses < 0:
            return False
    return conta_parenteses == 0


# Valores válidos
val = "()"
print(val, validador_parenteses(val))

val = "()()"
print(val, validador_parenteses(val))

val = "(())"
print(val, validador_parenteses(val))

val = "(()()())"
print(val, validador_parenteses(val))

val = "(((())()))"
print(val, validador_parenteses(val))

# Valores inválidos
val = ")"
print(val, validador_parenteses(val))

val = "("
print(val, validador_parenteses(val))

val = "()("
print(val, validador_parenteses(val))

val = "()()())"
print(val, validador_parenteses(val))

val = "(((())())"
print(val, validador_parenteses(val))
