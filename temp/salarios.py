def novo_salario(lista_salarios: list) -> list:
    pass


def test():
    assert novo_salario([]) == []
    assert novo_salario([-1, 1000]) == [1200]
    assert novo_salario([900, 2000, 2800, 5500]) == [1080, 2300, 3300, 5500]
