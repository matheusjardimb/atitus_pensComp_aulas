def busca_binaria_recursiva(lista: list, valor: int, inicio: int, fim: int) -> bool:
    if inicio > fim:
        return False

    meio = (inicio + fim) // 2

    if lista[meio] == valor:
        return True
    if lista[meio] < valor:
        return busca_binaria_recursiva(lista, valor, meio + 1, fim)
    return busca_binaria_recursiva(lista, valor, inicio, meio - 1)


# Função principal que inicia a busca
def busca_binaria(lista: list, valor: int) -> bool:
    return busca_binaria_recursiva(lista, valor, 0, len(lista) - 1)


# Exemplo de uso
lista_ordenada = [1, 3, 5, 7, 9, 11, 13, 15]
valor = 7

print(busca_binaria(lista_ordenada, valor))
