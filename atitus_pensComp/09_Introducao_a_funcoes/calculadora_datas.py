"""
Meses sao representados como: 1=Jan, 2=Feb, 3=Mar..
"""


def solicita_int(msg: str, min: int = 0, max: int | None = None) -> int:
    """
    Exibe a msg e solicita ao usuário um valor. Retorna o valor como inteiro
    """
    while True:
        if max is None:
            dica = f" (valor >={min})"
        else:
            dica = f" (valor >={min} e valor <={max})"

        valor = int(input(msg + dica + ": "))
        if valor < min:
            print(f"Valor deve ser >={min}, tente novamente")
        elif max is not None and valor > max:
            print(f"Valor deve ser <={max}, tente novamente")
        else:
            return valor


MESES_31_DIAS = [1, 3, 5, 7, 8, 10, 12]
MESES_30_DIAS = [4, 6, 9, 11]


def eh_bissexto(ano: int) -> bool:
    return ano % 4 == 0


def total_dias_no_mes(mes: int, ano: int) -> int:
    if mes in MESES_31_DIAS:
        return 31
    if mes in MESES_30_DIAS:
        return 30
    if eh_bissexto(ano):  # Fevereiro
        return 29
    return 28


def formata_data(data: list) -> str:
    return f"{data[0]}/{data[1]}/{data[2]}"


def solicita_data() -> list:
    """
    Solicita ao usuário e retorna uma data válida, representada como [dia, mes, ano]
    """
    print("")
    ano = solicita_int("Digite o ano")
    mes = solicita_int("Digite o mes", min=1, max=12)
    max_dia = total_dias_no_mes(mes, ano)
    dia = solicita_int("Digite o dia", min=1, max=max_dia)
    data = [dia, mes, ano]
    print(f"Data {formata_data(data)} digitada")
    return data


def converte_data_para_int(data: list) -> int:
    data_dia, data_mes, data_ano = data
    total_dias = 0
    for ano in range(1, data_ano):
        if eh_bissexto(ano):
            total_dias += 366
        else:
            total_dias += 365

    for mes in range(1, data_mes):
        total_dias += total_dias_no_mes(data_mes, data_ano)

    total_dias += data_dia
    return total_dias


def calcula_diferenca(data1: list, data2: list) -> int:
    data1_int = converte_data_para_int(data1)
    data2_int = converte_data_para_int(data2)
    return data2_int - data1_int  # diferenca em dias entre data1 e data2


# data_inicial = solicita_data()
data_inicial = [2, 7, 2004]
data_ini_str = formata_data(data_inicial)

# data_atual = solicita_data()
data_atual = [27, 5, 2024]
data_atual_str = formata_data(data_atual)

# data_final = solicita_data()
data_final = [2, 7, 2004 + 85]
data_final_str = formata_data(data_final)

# A quantidade de dias entre a data ‘inicial’ e ‘atual’
dif_ini_atual = calcula_diferenca(data_inicial, data_atual)
print(
    f"Diferenca em dias entre {data_ini_str} e {data_atual_str} é de {dif_ini_atual} dias"
)

# A quantidade de dias entre a data ‘atual’ e ‘final’
dif_atual_final = calcula_diferenca(data_atual, data_final)
print(
    f"Diferenca entre {data_atual_str} e {data_final_str} é de {dif_atual_final} dias"
)

# A quantidade de dias entre a data ‘inicial’ e ‘final’
dif_ini_final = calcula_diferenca(data_inicial, data_final)
print(f"Diferenca entre {data_ini_str} e {data_final_str} é de {dif_ini_final} dias")

# O percentual que a data ‘atual’ representa entre a ‘inicial’ e a ‘final’.
percentual = (1 - dif_atual_final / dif_ini_final) * 100
print(
    f"A data {data_atual_str} representa {percentual}% entre {data_ini_str} e {data_final_str}"
)
