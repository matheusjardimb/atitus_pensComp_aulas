def validador_parenteses(entrada: str) -> bool:
    pass


# Valores válidos
assert validador_parenteses("()")
assert validador_parenteses("()()")
assert validador_parenteses("(())")
assert validador_parenteses("(()()())")
assert validador_parenteses("(((())()))")

# Valores inválidos
assert validador_parenteses(")")
assert validador_parenteses("(")
assert validador_parenteses("()(")
assert validador_parenteses("()()())")
assert validador_parenteses("(((())())")
