MIN_IDADE_APOSENTADORIA = 62
MAX_SALARIO_MEI = 6750

ANO_ATUAL = 2024
# As linhas abaixo geram o '2024' de forma dinâmica (conteúdo do final do semestre)
# import datetime
# ANO_ATUAL = datetime.date.today().year

ano_nascimento = int(input("Digite o ano do seu nascimento: "))
idade = ANO_ATUAL - ano_nascimento

estuda = input("Você estuda (s/n)? ") == "s"
trabalha = input("Você trabalha (s/n)? ") == "s"

aposentado = False
regime = None
renda = None

if trabalha:
    regime = input("Qual regime de trabalho (mei/estag/outro)? ")
    renda = float(input("Qual sua renda mensal? "))
else:
    aposentado = input("Você é aposentado(s/n)? ") == "s"

if (
    (regime == "mei" and renda > MAX_SALARIO_MEI)
    or (regime == "estag" and not estuda)
    or (trabalha and idade < 14)
    or (trabalha and renda < 0)
    or (idade < 0 or idade > 150)
):
    print("Cadastro reprovado")
elif (
    (aposentado and idade < MIN_IDADE_APOSENTADORIA)
    or (idade < 14 and not estuda)
    or (trabalha and estuda and (14 <= idade <= 16))
):
    print("Cadastro aprovado com ressalvas")
else:
    print("Cadastro aprovado")
