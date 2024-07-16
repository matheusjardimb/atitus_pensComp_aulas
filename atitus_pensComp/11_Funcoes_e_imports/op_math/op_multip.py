def multiplicacao(a: int, b: int) -> int:
    negative_result = False
    if a < 0:
        a = -a
        negative_result = True
    if b < 0:
        b = -b
        negative_result = not negative_result

    result = 0
    for _ in range(b):
        result += a

    if negative_result:
        return -result
    return result
