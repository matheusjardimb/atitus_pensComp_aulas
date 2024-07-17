def busca_binaria(lista: list, valor: int) -> bool:
    inicio = 0
    fim = len(lista) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2

        if lista[meio] == valor:
            return True
        elif lista[meio] < valor:
            inicio = meio + 1
        else:
            fim = meio - 1

    return False


lista_ordenada = [1, 3, 5, 7, 9, 11, 13, 15]
valor = 7

print(busca_binaria(lista_ordenada, valor))
