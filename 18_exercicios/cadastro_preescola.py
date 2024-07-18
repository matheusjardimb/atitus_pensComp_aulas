IDADE_PARA_MAIORIDADE = 18


def verifica_maioridade(idade: int) -> bool:
    pass


def verifica_email(email: str) -> bool:
    pass


def solicita_nome() -> str | None:
    pass


# Testes para verifica_maioridade
assert not verifica_maioridade(-1)
assert not verifica_maioridade(0)
assert not verifica_maioridade(1)
assert not verifica_maioridade(17)
assert verifica_maioridade(18)
assert verifica_maioridade(20)
assert verifica_maioridade(100)

# Testes para verifica_email
assert not verifica_email('')
assert not verifica_email('@')
assert not verifica_email('@@')
assert not verifica_email('abc@@abc.com')
assert not verifica_email('abc@abc.edu')
assert not verifica_email('a_b_c@a_b_c.com.com')
assert not verifica_email('a_b_c@a_b_c.com.com.com')

assert verifica_email('ABC@a_b_c.com')
assert verifica_email('ABC@ABC.com')
assert verifica_email('AbC@1BC.com')
assert verifica_email('abc@abc.com')
assert verifica_email('a23@123.com')
assert verifica_email('a_b_c@a_b_c.com')
