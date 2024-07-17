# def saudacao(nome, idade=25, cidade='PoA'):
#     print(f'Olá, {nome}! Você tem {idade} anos e mora em {cidade}')
#
#
# saudacao('Matheus', 32, 'PoA')
# saudacao(32, 'Matheus', 'PoA')
# saudacao('Matheus', 32, cidade='PoA')
# saudacao(cidade='PoA', idade=32, nome='Matheus')
#
# saudacao(nome='Matheus', idade=32)
# saudacao(nome='Matheus')
#
#
# def potencia(base, expoente=2):
#     return base ** expoente
#
#
# print(potencia(10))
# print(potencia(10, 3))
# print(potencia(10, 4))
#
# variavel_global = 10
#
#
# def minha_funcao():
#     global variavel_global
#     variavel_local = 10
#     variavel_global = 20
#     print(variavel_local)
#
#
# minha_funcao()
# print(variavel_global)
#
#
#
#
#
#
#
#
#
#


def saudacao(nome: str, casado: bool) -> str:
    if casado:
        return f"Olá, Sr {nome}"
    return f"Olá, {nome}"


print(saudacao("matheus", True))
print(saudacao("Joao", False))


pares = [x for x in range(10) if x % 2 == 0]
