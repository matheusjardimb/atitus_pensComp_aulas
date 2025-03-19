from datetime import date


# Crie método que recebe uma string (mm-dd-aaaa) e retorna uma data
def str_to_date(date_str):
    pass


# O nome do dia da semana (“sábado”, “domingo”, …)
def nome_dia_semana(data):
    pass


# Quantos dias faltam para o final de semana
def dias_para_finde(data):
    pass


def test_dias_para_finde():
    assert dias_para_finde(date(year=2025, month=1, day=1)) == 3
    assert dias_para_finde(date(year=2025, month=1, day=2)) == 2


# Quantos dias existem entre a data e hoje
def delta_dias(data_a, data_b):
    pass


# O mesmo dia no próximo mês (ou o anterior próximo)
def proximo_mes(data_a):
    pass


# 1 se esta data está no futuro, -1 se no passado ou 0 se for hoje.
def data_futuro(data: date) -> str:
    pass


def test_delta_dias():
    assert (
        delta_dias(date(year=2025, month=1, day=1), date(year=2026, month=1, day=2))
        == 365
    )
    assert (
        delta_dias(date(year=2026, month=1, day=1), date(year=2025, month=1, day=2))
        == -365
    )
    assert (
        delta_dias(date(year=2025, month=1, day=1), date(year=2025, month=1, day=2))
        == 0
    )


def test_proximo_mes():
    assert proximo_mes(date(year=2025, month=1, day=1)) == date(
        year=2025, month=2, day=1
    )
    assert proximo_mes(date(year=2025, month=1, day=29)) == date(
        year=2025, month=2, day=28
    )
    assert proximo_mes(date(year=2024, month=1, day=29)) == date(
        year=2024, month=2, day=29
    )
    assert proximo_mes(date(year=2025, month=1, day=30)) == date(
        year=2025, month=2, day=28
    )


def test_str_to_date():
    assert str_to_date("10-01-2025") == date(day=10, month=1, year=2025)
    assert str_to_date("10-99-2025") is None


def test_nome_dia_semana():
    assert nome_dia_semana(date(year=2025, month=1, day=1)) == "quarta-feira"
    assert nome_dia_semana(date(year=2025, month=1, day=2)) == "quinta-feira"


def test_data_futuro():
    assert data_futuro(date(day=1, month=1, year=2099)) == 1
    assert data_futuro(date(day=1, month=1, year=1999)) == -1
    assert data_futuro(date.today()) == 0
