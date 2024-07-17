from op_inverte_sinal import inverte_sinal


# 10 // 3 = 3
def divisao(a: int, b: int) -> int | None:
    if b == 0:
        return None

    has_negative = False
    if a < 0:
        has_negative = True
        a = inverte_sinal(a)
    if b < 0:
        has_negative = not has_negative
        b = inverte_sinal(b)

    quotient = 0
    while a >= b:
        a -= b
        quotient += 1

    if has_negative:
        return inverte_sinal(quotient)
    return quotient


print(divisao(-10, 3))
