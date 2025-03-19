def busca_simples(lista: list, valor: int) -> bool:
    pass


def test():
    lista_ordenada = [1, 3, 5, 7, 9, 11, 13, 15]
    assert busca_simples(lista_ordenada, 1)
    assert busca_simples(lista_ordenada, 7)
    assert busca_simples(lista_ordenada, 15)

    assert not busca_simples(lista_ordenada, -1)
    assert not busca_simples(lista_ordenada, 47)
    assert not busca_simples(lista_ordenada, 999)
