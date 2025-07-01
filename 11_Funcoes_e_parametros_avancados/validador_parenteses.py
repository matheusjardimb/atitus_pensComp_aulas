def validador_parenteses(entrada: str) -> bool:
    pass


def test_validos():
    # Valores válidos
    assert validador_parenteses("()")
    assert validador_parenteses("()()")
    assert validador_parenteses("(())")
    assert validador_parenteses("(()()())")
    assert validador_parenteses("(((())()))")


def test_invalidos():
    # Valores inválidos
    assert not validador_parenteses(")")
    assert not validador_parenteses("(")
    assert not validador_parenteses("()(")
    assert not validador_parenteses("()()())")
    assert not validador_parenteses("(((())())")
