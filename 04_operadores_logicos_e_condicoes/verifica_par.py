def eh_par(numero):
    # Preencher
    pass


def eh_impar(numero):
    # Preencher
    # Use a função anterior
    pass


def test_eh_par():
    assert eh_par(0)
    assert eh_par(2)
    assert eh_par(4)
    assert not eh_par(1)
    assert not eh_par(3)


def test_eh_impar():
    assert eh_impar(1)
    assert eh_impar(3)
    assert eh_impar(5)
    assert not eh_impar(0)
    assert not eh_impar(2)
