# nome
nome = input("digite o seu nome:")
nome_cap = nome.capitalize()

while (
    (len(nome) < 3)
    or (nome != nome_cap)
    or ("1" in nome)
    or ("2" in nome)
    or ("3" in nome)
    or ("4" in nome)
    or ("5" in nome)
    or ("6" in nome)
    or ("7" in nome)
    or ("8" in nome)
    or ("9" in nome)
):
    nome = input("digite um nome válido:")
    nome_cap = nome.capitalize()

# sobrenome
sobrenome = input("digite o seu sobrenome:")
sobrenome_cap = sobrenome.capitalize()

while (
    (len(sobrenome) < 3)
    or (sobrenome != sobrenome_cap)
    or ("1" in sobrenome)
    or ("2" in sobrenome)
    or ("3" in sobrenome)
    or ("4" in sobrenome)
    or ("5" in sobrenome)
    or ("6" in sobrenome)
    or ("7" in sobrenome)
    or ("8" in sobrenome)
    or ("9" in sobrenome)
):
    sobrenome = input("digite um sobrenome válido:")
    sobrenome_cap = sobrenome.capitalize()

# email
email = input("digite seu email:")

while "@" not in email:
    email = input("digite um email válido:")

lista_email_nomesite = email.split("@")
email_nome = lista_email_nomesite[0]
email_site = lista_email_nomesite[1]

while (
    (len(lista_email_nomesite) != 2)
    or (len(email_nome) < 3 or len(email_nome) > 30)
    or (len(email_site) < 4 or len(email_site) > 20)
    or (email_site[(len(email_site) - 4) :] != ".com")
):
    email = input("digite um email válido:")

    while "@" not in email:
        email = input("digite um email válido:")

        lista_email_nomesite = email.split("@")
        email_nome = lista_email_nomesite[0]
        email_site = lista_email_nomesite[1]

print("cadastro aprovado")
