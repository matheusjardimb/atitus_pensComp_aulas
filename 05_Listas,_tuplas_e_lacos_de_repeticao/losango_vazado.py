altura = int(input("Digite um valor ímpar para a altura do losango: "))

if (
    altura % 2 == 0
):  # Se a altura for par, incrementa em 1 para garantir uma linha central
    altura += 1
    print("O valor digitado era par, usaremos", altura, "no lugar")

meio = altura // 2  # Meio do losango

for linha_atual in range(altura):
    if linha_atual <= meio:  # Parte superior do losango
        num_espacos = meio - linha_atual
        num_star = linha_atual * 2 + 1
    else:  # Parte inferior do losango
        num_espacos = linha_atual - meio
        num_star = altura - (linha_atual - meio) * 2

    linha = " " * num_espacos
    for j in range(num_star):
        if j % 2 == 0:
            linha += "*"
        else:
            linha += " "
    linha += " " * num_espacos
    print(linha)
