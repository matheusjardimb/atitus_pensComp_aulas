def saudacao(nome, sobrenome, titulo):
    pass


assert saudacao("Matheus") == "Olá, Matheus"
assert saudacao("Matheus", "Jardim") == "Olá, Matheus Jardim"
assert saudacao("Matheus", "Jardim", "Prof") == "Olá, Prof Matheus Jardim"
assert saudacao("Matheus", titulo="Prof") == "Olá, Prof Matheus"
assert saudacao("") == "Olá!"
