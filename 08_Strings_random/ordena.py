def ordena_lista(lista):
    pass


def ordena_lista_nova(lista):
    pass


def test_ordena_lista():
    assert ordena_lista([]) == []
    assert ordena_lista([1]) == [1]
    assert ordena_lista([4, 3, 2, 2, 1, 0]) == [0, 1, 2, 2, 3, 4]
    assert ordena_lista([10, 0, -3, 42, 5, -6, 8, 91]) == [-6, -3, 0, 5, 8, 10, 42, 91]


def test_ordena_lista_nova():
    assert ordena_lista_nova([]) == []
    assert ordena_lista_nova([1]) == [1]
    assert ordena_lista_nova([4, 3, 2, 2, 1, 0]) == [0, 1, 2, 2, 3, 4]
    assert ordena_lista_nova([10, 0, -3, 42, 5, -6, 8, 91]) == [
        -6,
        -3,
        0,
        5,
        8,
        10,
        42,
        91,
    ]
