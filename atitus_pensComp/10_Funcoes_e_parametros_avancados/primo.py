def eh_primo(numero: int) -> bool:
    # Caso o número seja menor ou igual a 1, não é primo
    if numero <= 1:
        return False
    # Iteramos de 2 até o número - 1
    for i in range(2, numero):
        # Se o número for divisível por algum número diferente de 1 e ele mesmo, não é primo
        if numero % i == 0:
            return False
    # Se passar por todos os números sem ser divisível por nenhum, é primo
    return True


def lista_primos(x: int) -> list:
    result = []
    for x in range(x + 1):
        if eh_primo(x):
            result.append(x)
    return result


resultado = lista_primos(100)
print(resultado)  # [ 2, 3, 5, 7, 11, 13 ... ]
