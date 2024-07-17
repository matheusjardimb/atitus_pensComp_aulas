####################
def divisao(dividendo, divisor):
    quociente = dividendo // divisor
    resto = dividendo % divisor
    return quociente, resto


resultado = divisao(10, 3)
print(resultado)  # Saída: (3, 1)

quociente, resto = divisao(10, 3)
print(quociente, resto)  # Saída: 3 1


####################
def divisao(dividendo, divisor):
    return dividendo / divisor


# quociente, resto = divisao(10, 3)
# print(quociente, resto)  # Saída: 3 1


####################


def cadastrar_usuario(nome, cidade):
    print(f"Nome: {nome}, Cidade: {cidade}")


cadastrar_usuario("Augusto Pestana", "Maximiliano de Almeida")
cadastrar_usuario("Maximiliano de Almeida", "Augusto Pestana")


#################3
def adicionar_item(lista, item):
    lista.append(item)


minha_lista = [1, 2, 3]
print(minha_lista)  # Saída: [1, 2, 3]

adicionar_item(minha_lista, 4)
print(minha_lista)  # Saída: [1, 2, 3, 4]


######
def soma_um(val):
    return val + 1


val = 4
print(soma_um(val))  # Saída: 5
print(val)  # Saída: 4

########

soma = lambda x, y: x + y  # noqa
print(soma(3, 4))  # Saída: 7

quadrado = lambda x: x**2  # noqa
print(quadrado(5))  # Saída: 25

par = lambda x: x % 2 == 0  # noqa
print(par(6))  # Saída: True
print(par(7))  # Saída: False
