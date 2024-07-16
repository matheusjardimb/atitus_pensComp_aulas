"""
Implementa a Cifra de Cesar. Considera APENAS letras maiúsculas (ignora outros caracteres).
"""

POS_LETRA_Z = 90
POS_LETRA_A = 65
NUM_LETRAS_ALFABETO = 26

TEXTO_ORIGINAL = "TEXTO ZICA"
print("Original:", TEXTO_ORIGINAL)

######################################
# Cifra o texto
######################################
SHIFT = 9
texto_cifrado = ""
for char in TEXTO_ORIGINAL:
    # Verificamos se está entre A..Z. Senão, ignoramos.
    is_uppercase = POS_LETRA_A <= ord(char) <= POS_LETRA_Z
    if is_uppercase:  # o mesmo que: char.isupper()
        posicao_no_alfabeto_nova_letra = ord(char) - POS_LETRA_A + SHIFT
        shifted_char = chr(
            posicao_no_alfabeto_nova_letra % NUM_LETRAS_ALFABETO + POS_LETRA_A
        )
        texto_cifrado += shifted_char
    else:
        texto_cifrado += char
print("Cifrado:", texto_cifrado)

######################################
# Decifra o texto
######################################
SHIFT = -9
texto_decifrado = ""
for char in texto_cifrado:
    if POS_LETRA_A <= ord(char) <= POS_LETRA_Z:  # Verifica se está entre A..Z
        shifted_char = chr(
            (ord(char) - POS_LETRA_A + SHIFT) % NUM_LETRAS_ALFABETO + POS_LETRA_A
        )
        texto_decifrado += shifted_char
    else:
        texto_decifrado += char
print("Decifrado:", texto_decifrado)
