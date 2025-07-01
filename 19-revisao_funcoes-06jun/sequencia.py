def sequencia(param: list) -> bool:
    pass


def test():
    assert not sequencia([])
    assert not sequencia([1, 3])
    assert not sequencia([1, 2, 5])

    assert sequencia([1])
    assert sequencia([1, 2])
    assert sequencia([2, 1, 3])
    assert sequencia([9, 11, 12, 10])
