def consecutivos(lista: list) -> bool:
    pass


def test():
    assert not consecutivos([])
    assert not consecutivos([1])
    assert not consecutivos([1, 3])
    assert not consecutivos([1, 3, 5])

    assert consecutivos([1, 2])
    assert consecutivos([1, 3, 4])
    assert consecutivos([1, 2, 3])
    assert consecutivos([0, 2, 4, 6, 7, 8])
    assert consecutivos([0, 2, 4, 6, 8, 9])
