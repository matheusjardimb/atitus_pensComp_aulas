IDADE_PARA_MAIORIDADE = 18


def verifica_maioridade(idade: int) -> bool:
    """
    Verifica se a idade informada atingiu a maioridade (ver IDADE_PARA_MAIORIDADE)
    """
    return idade >= IDADE_PARA_MAIORIDADE


def verifica_email(email: str) -> bool:
    if email.count("@") != 1:
        return False
    email = email.lower()
    nome, site = email.split("@")

    if site.count(".com") != 1:
        return False
    if not site.endswith(".com"):
        return False
    site = site.replace(".com", "")

    chars_validos = "abcdefghijklmnopqrstuvwxyz01234567890_"
    for char in nome:
        if char not in chars_validos:
            return False
    for char in site:
        if char not in chars_validos:
            return False

    return True


def solicita_nome() -> str | None:
    # TODO considerar input com dois espacos em branco
    # TODO considerar caracteres especiais no input
    nome = None
    while nome is None:
        nome = input("Digite o nome completo: ")
        if nome == "":
            return None
        if " " not in nome:
            nome = None
            continue
        partes_do_nome = nome.split(" ")
        result = []
        for parte in partes_do_nome:
            result.append(parte.capitalize())
        return " ".join(result)
    return nome


print(solicita_nome())

# # Testes para verifica_maioridade
# print(verifica_maioridade(-1) == False)
# print(verifica_maioridade(0) == False)
# print(verifica_maioridade(1) == False)
# print(verifica_maioridade(17) == False)
# print(verifica_maioridade(18) == True)
# print(verifica_maioridade(20) == True)
# print(verifica_maioridade(100) == True)
#
# # Testes para verifica_email
# print(verifica_email('') == False)
# print(verifica_email('@') == False)
# print(verifica_email('@@') == False)
# print(verifica_email('abc@@abc.com') == False)
# print(verifica_email('abc@abc.edu') == False)
# print(verifica_email('a_b_c@a_b_c.com.com') == False)
# print(verifica_email('a_b_c@a_b_c.com.com.com') == False)
#
# print(verifica_email('ABC@a_b_c.com') == True)
# print(verifica_email('ABC@ABC.com') == True)
# print(verifica_email('AbC@1BC.com') == True)
# print(verifica_email('abc@abc.com') == True)
# print(verifica_email('a23@123.com') == True)
# print(verifica_email('a_b_c@a_b_c.com') == True)
