def kmh_para_ms(valor_kmh):
    pass


def ms_para_kmh(valor_ms):
    pass


def converter(valor, unidade):
    pass


def test():
    assert converter(1, "erro") is None
    assert converter(3.6, "k") == 1.0
    assert converter(1, "m") == 3.6
