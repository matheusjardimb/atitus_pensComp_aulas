def procura_numero(tabela: list, numero: int) -> bool:
    pass


def test():
    tabela = [
        [1, 2, 3],
        [4],
        [5, 6, 7, 8, 9, 10],
    ]
    assert procura_numero(tabela, 1)
    assert procura_numero(tabela, 3)
    assert procura_numero(tabela, 4)
    assert procura_numero(tabela, 5)
    assert procura_numero(tabela, 10)

    assert not procura_numero(tabela, 0)
    assert not procura_numero(tabela, -1)
