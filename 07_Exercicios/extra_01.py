def letra_em_texto(texto, letra):
    # Se esta letra existe dentro do texto (sem usar 'in')
    pass


def conta_letra_em_texto(texto, letra):
    # Quantas vezes essa letra aparece no texto (sem usar '.count()')
    pass


def texto_sem_letra(texto, letra):
    # O texto novamente, removendo todas ocorrências desta letra (sem usar 'replace()')
    pass


def texto_com_letra_upper(texto, letra):
    # O texto novamente, trocando essa letra por usa versão maiúscula  (sem usar 'replace()')
    pass


assert letra_em_texto("Pensamento Computacional", "a")
assert letra_em_texto("Pensamento Computacional", " ")
assert not letra_em_texto("Pensamento Computacional", "A")
assert not letra_em_texto("Pensamento Computacional", "c")

assert conta_letra_em_texto("Pensamento Computacional", "a") == 3
assert conta_letra_em_texto("Pensamento Computacional", "A") == 0
assert conta_letra_em_texto("Pensamento Computacional", "e") == 2

assert texto_sem_letra("Pensamento Computacional", "a") == "Pensmento Computcionl"
assert texto_sem_letra("Pensamento Computacional", "z") == "Pensamento Computacional"
assert texto_sem_letra("Pensamento Computacional", " ") == "PensamentoComputacional"

assert (
    texto_com_letra_upper("Pensamento Computacional", "a") == "PensAmento ComputAcionAl"
)
assert (
    texto_com_letra_upper("Pensamento Computacional", "z") == "Pensamento Computacional"
)
assert (
    texto_com_letra_upper("Pensamento Computacional", " ") == "Pensamento Computacional"
)
