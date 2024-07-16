"""
0- Solicite ao usuário o nome, sobrenome e ano de nascimento. Imprima:
    “Olá, <nome> <sobrenome>. Bom dia! Você possui <idade> anos“
"""

from datetime import date

nome = input("Digite seu nome: ")
sobrenome = input("Digite seu sobrenome: ")
ano_nascimento = int(input("Digite seu ano de nascimento: "))

ano_atual = date.today().year
idade = ano_atual - ano_nascimento
print(f"Olá, {nome} {sobrenome}. Bom dia! Você possui {idade} anos")
