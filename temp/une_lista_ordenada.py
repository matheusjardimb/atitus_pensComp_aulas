def une_listas(list_a: list, list_b: list) -> list:
    pass


def test():
    assert une_listas([], []) == []
    assert une_listas([1], []) == [1]
    assert une_listas([], [2]) == [2]
    assert une_listas([1], [2]) == [1, 2]
    assert une_listas([1], [1]) == [1, 1]
    assert une_listas([2, 4, 6], [1, 3, 5]) == [1, 2, 3, 4, 5, 6]
