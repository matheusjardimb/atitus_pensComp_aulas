def menor_num(lista: list) -> int | None:
    pass


def test():
    assert menor_num([]) is None
    assert menor_num([1, 1]) == 1
    assert menor_num([1, 2, 3]) == 1
    assert menor_num([1, 2, -3, 4]) == -3
