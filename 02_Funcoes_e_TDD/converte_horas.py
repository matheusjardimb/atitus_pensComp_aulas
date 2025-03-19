def hora_para_minuto(valor):
    # TODO: preencher
    pass


def minuto_para_segundo(valor):
    # TODO: preencher
    pass


def hora_para_segundo(valor):
    # TODO: preencher, deve usar minuto_para_segundo()
    pass


def dia_para_segundo(valor):
    # TODO: preencher, deve usar hora_para_segundo()
    pass


def test():
    assert hora_para_minuto(0) == 0
    assert hora_para_minuto(1) == 60
    assert hora_para_minuto(2) == 120

    assert minuto_para_segundo(0) == 0
    assert minuto_para_segundo(1) == 60
    assert minuto_para_segundo(2) == 120

    assert hora_para_segundo(0) == 0
    assert hora_para_segundo(1) == 3600  # 1 * 60 * 60
    assert hora_para_segundo(2) == 7200  # 2 * 60 * 60
    assert hora_para_segundo(5) == 18000  # 5 * 60 * 60

    assert dia_para_segundo(0) == 0
    assert dia_para_segundo(1) == 86400
    assert dia_para_segundo(2) == 172800
    assert dia_para_segundo(5) == 432000

    print("Terminou com sucesso!")
