def calcula_classe_social(salarios, salario_minimo):
    pass


assert calcula_classe_social([], 1000) is None
assert calcula_classe_social([1000], 1000) == "E"
assert calcula_classe_social([500], 1000) == "E"
assert calcula_classe_social([500], 1000) == "E"
assert calcula_classe_social([1000, 0], 900) == "E"
assert calcula_classe_social([1000], 900) == "D"
assert calcula_classe_social([10000, 15000], 1000) == "B"
assert calcula_classe_social([20000, 25000], 1000) == "A"
assert calcula_classe_social([20000, 0, 0, 0, 0], 1000) == "C"
