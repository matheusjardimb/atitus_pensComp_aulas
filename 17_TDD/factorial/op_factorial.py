def factorial(n: int) -> int | None:
    """
    Calcula o fatorial de número >= 0

    Parâmetros:
      n: int >= 0 para calcular

    Retorna:
      n! para n >= O
      None para n < O
    """
    if not isinstance(n, int) or n < 0:
        return None
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado
