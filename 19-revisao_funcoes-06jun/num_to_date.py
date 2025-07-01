def num_to_date(val: int) -> dict:
    pass


def test():
    assert num_to_date(-1) == {"dias": 0, "horas": 0, "minutos": 0, "segundos": 0}
    assert num_to_date(0) == {"dias": 0, "horas": 0, "minutos": 0, "segundos": 0}
    assert num_to_date(30) == {"dias": 0, "horas": 0, "minutos": 0, "segundos": 30}
    assert num_to_date(90) == {"dias": 0, "horas": 0, "minutos": 1, "segundos": 30}
    assert num_to_date(610) == {"dias": 0, "horas": 0, "minutos": 10, "segundos": 10}
    assert num_to_date(7200) == {"dias": 0, "horas": 2, "minutos": 0, "segundos": 0}
    assert num_to_date(183690) == {"dias": 2, "horas": 3, "minutos": 1, "segundos": 30}
