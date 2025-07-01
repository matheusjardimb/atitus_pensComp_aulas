def date_to_str(param: dict) -> str:
    pass


def test():
    assert date_to_str({"dias": 0, "horas": 0, "minutos": 0, "segundos": 0}) == ""
    assert (
        date_to_str({"dias": 0, "horas": 0, "minutos": 0, "segundos": 30})
        == "30 segundos"
    )
    assert (
        date_to_str({"dias": 0, "horas": 0, "minutos": 1, "segundos": 30})
        == "1 minuto e 30 segundos"
    )
    assert (
        date_to_str({"dias": 0, "horas": 0, "minutos": 10, "segundos": 10})
        == "10 minutos e 10 segundos"
    )
    assert (
        date_to_str({"dias": 0, "horas": 2, "minutos": 0, "segundos": 0}) == "2 horas"
    )
    assert date_to_str({"dias": 1, "horas": 0, "minutos": 0, "segundos": 0}) == "1 dia"
