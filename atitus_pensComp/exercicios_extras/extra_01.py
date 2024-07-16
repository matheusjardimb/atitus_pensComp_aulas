"""
1 - Solicite ao usuário um texto e uma letra. Informe:
"""

texto = input("Digite um texto: ")
letra = input("Digite uma letra: ")

# - Imprima se esta letra existe dentro do texto.
print(f'A letra "{letra}" está no texto?', letra in texto)

# - Imprima quantas vezes essa letra aparece no texto.
print(f'Quantas vezes "{letra}" aparece no texto?', texto.count(letra))

# - Imprima a frase novamente, removendo todas ocorrências desta letra
print(f'Frase sem "{letra}":', texto.replace(letra, ""))

# - Imprima a frase novamente, trocando essa letra por usa versão maiúscula
letra_upper = letra.upper()
print(
    f'Frase com "{letra_upper}" em vez de "{letra}":', texto.replace(letra, letra_upper)
)
