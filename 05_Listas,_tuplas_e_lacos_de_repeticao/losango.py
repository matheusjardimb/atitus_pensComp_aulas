altura = int(input("Digite um valor ímpar para a altura do losango: "))
if (
    altura % 2 == 0
):  # Se a altura for par, incrementa em 1 para garantir uma linha central
    altura += 1
    print("O valor digitado era par, usaremos", altura, "no lugar")

meio = altura // 2  # Linha do meio do losango (considere que a contagem inicia em 0)
for linha_atual in range(altura):  # Itera de 0 até altura
    if (
        linha_atual <= meio
    ):  # Desenhando a parte superior do losango (primeira linha até meio, incluindo o meio)
        num_espacos = meio - linha_atual
        num_star = linha_atual * 2 + 1
    else:  # Desenhando parte inferior do losango
        num_espacos = linha_atual - meio
        num_star = altura - (linha_atual - meio) * 2
    print("." * num_espacos + "#" * num_star)
