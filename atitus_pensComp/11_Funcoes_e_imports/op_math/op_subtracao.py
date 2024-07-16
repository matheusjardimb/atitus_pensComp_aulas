from op_inverte_sinal import inverte_sinal


def subtracao(valor1: int, valor2: int) -> int:
    return valor1 + inverte_sinal(valor2)


print(subtracao(10, 2))
