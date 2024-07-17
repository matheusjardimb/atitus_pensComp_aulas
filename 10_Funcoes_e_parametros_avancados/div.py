# def divisao_com_resto(dividendo, divisor):
#     quociente = dividendo // divisor
#     resto = dividendo % divisor
#     return quociente, resto
#
#
# def divisao(dividendo, divisor):
#     return dividendo / divisor
#
#
# quociente, resto = divisao_com_resto(10, 3)
# print(quociente, resto)
#
# resultado = divisao_com_resto(10, 3)
# print(resultado)
#
#
#
#
# def cadastra_usuario(nome, idade=0, cidade='PoA'):
#     return f'Nome {nome}, idade {idade} cidade {cidade}'
#
#
# print(cadastra_usuario('Matheus', 22, 'Sao Paulo'))
# print(cadastra_usuario(nome='Matheus', idade=22, cidade='Sao Paulo'))


def soma_um(val):
    val = val + 1
    return val


val = 5
print(val)
print(soma_um(val))
print(val)


def adicionar_item(lista, item):
    lista.append(item)


minha_lista = [1, 2, 3]
print(minha_lista)

adicionar_item(minha_lista, 4)
print(minha_lista)

adicionar_item(minha_lista, 5)
print(minha_lista)

adicionar_item(minha_lista, 6)
print(minha_lista)
