def sao_anagramas_v1(palavra1: str, palavra2: str) -> bool:
    if len(palavra1) != len(palavra2):
        return False

    for char in palavra1:
        if char not in palavra2:
            return False
        palavra2 = palavra2.replace(char, "", 1)
    return len(palavra2) == 0


print(sao_anagramas_v1("banana", "anana"))  # False
print(sao_anagramas_v1("amor", "roma"))  # True
print(sao_anagramas_v1("iracema", "america"))  # True
print(sao_anagramas_v1("estudo", "duetos"))  # True


def sao_anagramas_v2(palavra1: str, palavra2: str) -> bool:
    # Remove espaços e converte para minúsculas
    palavra1 = palavra1.replace(" ", "").lower()
    palavra2 = palavra2.replace(" ", "").lower()

    # Verifica se os comprimentos são diferentes
    if len(palavra1) != len(palavra2):
        return False

    # Ordena as letras de ambas as palavras e compara
    return sorted(palavra1) == sorted(palavra2)


print(sao_anagramas_v2("banana", "anana"))  # False
print(sao_anagramas_v2("amor", "roma"))  # True
print(sao_anagramas_v2("iracema", "america"))  # True
print(sao_anagramas_v2("estudo", "duetos"))  # True
