def fahrenheit_para_celsius(valor):
    pass


def celsius_para_fahrenheit(valor):
    pass


def test_fahrenheit_para_celsius():
    assert fahrenheit_para_celsius(104) == 40
    assert fahrenheit_para_celsius(-13) == -25


def test_celsius_para_fahrenheit():
    assert celsius_para_fahrenheit(40) == 104
    assert celsius_para_fahrenheit(-25) == -13


def test_geral():
    assert celsius_para_fahrenheit(fahrenheit_para_celsius(15)) == 15
    assert celsius_para_fahrenheit(fahrenheit_para_celsius(30)) == 30
