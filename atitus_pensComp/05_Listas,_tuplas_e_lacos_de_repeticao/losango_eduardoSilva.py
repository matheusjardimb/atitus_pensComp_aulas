# By Eduardo Silva <1136768@atitus.edu.br>

altura = int(input("Digite um número ímpar para formar um losango: "))

if (
    altura % 2 == 0
):  # Se a altura for par, incrementa em 1 para garantir uma linha central
    altura += 1
    print("O valor digitado era par, usaremos", altura, "no lugar")

metade = altura // 2
# Desenha a metade superior, incluindo até a linha mais larga
for linha in range(metade + 1):
    qtd_espacos = metade - linha
    qtd_star = (2 * linha) + 1
    print("." * qtd_espacos + "#" * qtd_star)

# Desenha a metade inferior
for linha in range(metade):
    qtd_espacos = linha + 1
    qtd_star = (altura - 2) - (2 * linha)
    print("." * qtd_espacos + "#" * qtd_star)
