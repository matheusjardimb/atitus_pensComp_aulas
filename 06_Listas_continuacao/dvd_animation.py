def limpa_tela():
    import os

    os.system("cls" if os.name == "nt" else "clear")  # Limpa o console


def espera():
    import time

    time.sleep(5)  # Espera meio segundo (500ms)


def desenha_tela():
    # Preencher
    pass


def main():
    # Loop?
    limpa_tela()
    espera()
    desenha_tela()


main()
