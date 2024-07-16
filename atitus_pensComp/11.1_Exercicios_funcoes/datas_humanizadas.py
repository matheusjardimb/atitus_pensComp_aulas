"""
Datas humanizadas
    Escreva uma função que recebe um valor inteiro que representa uma quantidade de segundos. Retorne uma string que converta esse valor para uma forma apresentável:
    Até 60s -> “x segundos”
    Exatos 60s   -> “1 minuto”
    Múltiplos de 60s   -> “x minutos”
    Até 1h   -> “y minutos e x segundos”
    Mais de 1h -> “z horas, y minutos e x segundos”

"""

MINUTO = 60
HORA = 60 * MINUTO


def msg_plural(valor, singular_msg, plural_msg):
    if valor == 0:
        return ""
    if valor == 1:
        return singular_msg
    return plural_msg


def data_humanizada(duracao: int) -> str:
    horas = duracao // HORA
    duracao = duracao - horas * HORA
    horas_msg = msg_plural(horas, f"{horas} hora", f"{horas} horas")

    minutos = duracao // MINUTO
    duracao = duracao - minutos * MINUTO
    minutos_msg = msg_plural(minutos, f"{minutos} minuto", f"{minutos} minutos")

    segundos = duracao % MINUTO
    segundos_msg = msg_plural(segundos, f"{segundos} segundo", f"{segundos} segundos")

    return f"{horas_msg} {minutos_msg} {segundos_msg}".strip()


print(data_humanizada(10))
print(data_humanizada(1 * MINUTO))
print(data_humanizada(2 * MINUTO))
print(data_humanizada(2 * MINUTO + 20))
print(data_humanizada(2 * HORA + 3 * MINUTO + 20))
