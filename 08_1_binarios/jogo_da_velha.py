def imprime_tabuleiro(tabuleiro):
    print()
    for linha in tabuleiro:
        print(" ".join(linha))
    print()


def verifica_vencedor(tabuleiro):
    # Verifica linhas
    for linha in tabuleiro:
        if linha[0] == linha[1] and linha[0] == linha[2]:
            return linha[0]

    # Verifica colunas
    for i in range(3):
        if tabuleiro[0][i] == tabuleiro[1][i] and tabuleiro[0][i] == tabuleiro[2][i]:
            return tabuleiro[0][i]

    # Verifica diagonais
    if tabuleiro[0][0] == tabuleiro[1][1] and tabuleiro[0][0] == tabuleiro[2][2]:
        return tabuleiro[0][0]
    if tabuleiro[0][2] == tabuleiro[1][1] and tabuleiro[0][2] == tabuleiro[2][0]:
        return tabuleiro[0][2]

    for linha in tabuleiro:
        for celula in linha:
            if celula != "X" and celula != "O":
                # Não há vencedor e há celulas para marcar
                return None

    return "E"  # Empate


def registra_jogada(tabuleiro, jogador_atual):
    simbolo_jogador = obtem_simbolo_jogador(jogador_atual)
    while True:
        jogada = input(f"Jogador '{simbolo_jogador}', escolha a celula para jogar: ")
        for linha in [0, 1, 2]:
            for coluna in [0, 1, 2]:
                if tabuleiro[linha][coluna] == jogada:
                    tabuleiro[linha][coluna] = simbolo_jogador
                    return
        print("Opção inválida")


def obtem_simbolo_jogador(jogador_atual):
    if jogador_atual % 2 == 0:
        return "X"
    return "O"


def iniciar_jogo():
    tabuleiro = [
        ["0", "1", "2"],
        ["3", "4", "5"],
        ["6", "7", "8"],
    ]

    jogador_atual = 1
    vencedor = None
    while vencedor is None:
        imprime_tabuleiro(tabuleiro)
        registra_jogada(tabuleiro, jogador_atual)
        jogador_atual += 1
        vencedor = verifica_vencedor(tabuleiro)

    imprime_tabuleiro(tabuleiro)
    if vencedor == "E":
        print("Empate")
    else:
        print(f"Vitória de {vencedor}")


iniciar_jogo()
