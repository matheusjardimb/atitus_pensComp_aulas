def fahrenheit_para_celsius(valor):
    pass


def celsius_para_fahrenheit(valor):
    pass


assert fahrenheit_para_celsius(104) == 40
assert fahrenheit_para_celsius(-13) == -25

assert celsius_para_fahrenheit(40) == 104
assert celsius_para_fahrenheit(-25) == -13

assert celsius_para_fahrenheit(fahrenheit_para_celsius(30)) == 30
