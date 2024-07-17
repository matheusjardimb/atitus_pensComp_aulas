"""
6- Solicite ao usuário uma palavra e uma letra.
"""

palavra = input("Digite uma palavra: ")
letra = input("Digite uma letra: ")

# - Imprima se a letra existe dentro da palavra.
if letra in palavra:
    print(f'A letra "{letra}" está contida na palavra "{palavra}"')
    # - Imprima quantas vezes a letra ocorre na palavra
    print(
        f'A letra "{letra}" está contida {palavra.count(letra)} na palavra "{palavra}"'
    )
else:
    print(f'A letra "{letra}" não está contida na palavra "{palavra}"')

# - Imprima a palavra toda em maiúsculo
print(f"Versão maiúscula: {palavra.upper()}")

# - Imprima a palavra toda em minúsculo
print(f"Versão maiúscula: {palavra.lower()}")

# - Imprima se a letra é maiúscula ou minúscula
if letra.isupper():
    print(f'Letra "{letra}" é maiúscula')
else:
    print(f'Letra "{letra}" é minúscula')
