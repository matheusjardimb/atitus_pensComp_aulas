def imprimir_calendario_mes(dia_inicial: int, total_dias: int):
    dias_da_semana = ["Do", "Se", "Te", "Qu", "Qu", "Se", "Sá"]

    # Imprimir o cabeçalho com os dias da semana
    print(" ".join(dias_da_semana))

    # Criar a lista inicial do calendário com espaços vazios para os dias antes do início do mês
    calendario = ["  "] * dia_inicial

    # Adicionar os dias do mês ao calendário
    for dia in range(1, total_dias + 1):
        calendario.append(str(dia).rjust(2, " "))

    # Imprimir o calendário
    while len(calendario) > 0:
        semana = calendario[:7]
        print(" ".join(semana))
        calendario = calendario[7:]


# Exemplo de uso
# dia_inicial = int(input("Digite o dia inicial da semana (0=Do, 1=Se, ..., 6=Sá): "))
# total_dias = int(input("Digite o número total de dias no mês: "))
# imprimir_calendario_mes(dia_inicial, total_dias)

for d in range(0, 7):
    imprimir_calendario_mes(d, 31)
