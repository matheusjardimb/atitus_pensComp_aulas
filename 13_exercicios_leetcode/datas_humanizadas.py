MINUTO = 60
HORA = 60 * MINUTO


def data_humanizada(duracao: int) -> str:
    pass


assert data_humanizada(10) == "10 segundos"
assert data_humanizada(1 * MINUTO) == "1 minuto"
assert data_humanizada(2 * MINUTO) == "2 minutos"
assert data_humanizada(2 * MINUTO + 20) == "2 minutos 20 segundos"
assert data_humanizada(2 * HORA + 3 * MINUTO + 20) == "2 horas 3 minutos 20 segundos"
