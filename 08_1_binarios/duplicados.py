def encontra_duplicados(lista):
    pass


def test_encontra_duplicados():
    assert not encontra_duplicados([])
    assert not encontra_duplicados([1])
    assert not encontra_duplicados([1, 2])
    assert encontra_duplicados([1, 2, 3, 1])
    assert encontra_duplicados([1, 2, 3, 3, 2, 1])


def lista_duplicados(lista):
    pass


def test_lista_duplicados():
    assert lista_duplicados([]) == []
    assert lista_duplicados([1]) == []
    assert lista_duplicados([1, 2]) == []
    assert lista_duplicados([1, 2, 3, 1]) == [1]
    assert lista_duplicados([1, 2, 3, 3, 2, 1]) == [3, 2, 1]
