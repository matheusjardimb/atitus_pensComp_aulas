"""
Recebe uma lista de valores inteiros L e um valor inteiro N.
Retorna uma lista com a combinação de valores de L que, quando somados, se igualam a N.
Se não houver combinação encontrada, retorna [].
"""


def total(dados: int | list) -> int:
    """
    Retorna um inteiro contendo a soma de todos os valores, somando inclusive os itens dentro de listas encadeadas.
    """
    if isinstance(dados, int):
        return dados

    result = 0
    for dado in dados:
        result += total(dado)
    return result


def soma_pares(numeros: list, alvo: int) -> list:
    aux = []
    for x in numeros:
        total_x = total(x)
        if total_x < alvo:
            aux.append(x)
        for y in numeros:
            total_y = total(y)
            soma_xy = total_x + total_y
            if soma_xy == alvo:
                return [x, y]
            if soma_xy < alvo and [x, y] not in numeros and [y, x] not in numeros:
                aux.append([x, y])

    list_total = []
    new_aux = []
    for elem in aux:
        total_elem = total(elem)
        if total_elem not in list_total:
            list_total.append(total_elem)
            new_aux.append(elem)
    if len(aux) == 0 or total(aux) < alvo or numeros == aux or numeros == new_aux:
        return []
    return soma_pares(new_aux, alvo)


def to_simple_list(a: list) -> list:
    """
    Concatena todos os elementos de 'a' em uma lista, removendo as listas encadeadas.
    """
    my_list = []
    for element in a:
        if isinstance(element, int):
            my_list += [element]
        else:
            my_list += to_simple_list(element)
    return my_list


# Lista todos os valores de 0 a 100, e uma combinação possível de valores que somados igualam ao alvo (caso exista).
for val in range(101):
    res = soma_pares([3, 5, 8], val)
    print(val, to_simple_list(res))
