def caesar_cipher(texto, desvio):
    result = ""
    for char in texto:
        if char.isalpha():  # Avalia se é letra (a..z, A..Z)
            # Acrescenta um 'offset' de 65 se for maiúsculo e 97 do contrário
            ascii_offset = 65 if char.isupper() else 97
            shifted_char = chr((ord(char) - ascii_offset + desvio) % 26 + ascii_offset)
            result += shifted_char
        else:
            result += char
    return result


shift = 3
plaintext = "Hello, World!"
print("Original:", plaintext)

cipher_text = caesar_cipher(plaintext, shift)
print("Ciphered:", cipher_text)

plaintext = caesar_cipher(cipher_text, -shift)
print("Deciphered:", plaintext)
