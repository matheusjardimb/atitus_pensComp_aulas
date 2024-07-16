# Solicite ao usuário uma data no formato dd/mm/aaaa e crie uma função para cada item abaixo:
# Imprima a data no formato mm-dd-aa
# Imprima se esta data está no futuro, passado ou é hoje
# Imprima o nome do dia da semana (“sábado”, “domingo”, …)
# Imprima quantos dias faltam para o final de semana
# Imprima quantos dias existem entre esta data e hoje
# Imprima este dia no próximo mês
import datetime


def formata_data(data: datetime.date) -> str:
    # Imprima a data no formato mm-dd-aa
    return data.strftime("%m-%d-%y")


def data_futuro(data: datetime.date) -> str:
    # Imprima se esta data está no futuro, passado ou presente
    data_hoje = datetime.date.today()
    if data == data_hoje:
        return "Presente"
    if data > data_hoje:
        return "Futuro"
    return "Passado"


data_str = input("Informe uma data no formato mm/dd/aaaa")

data = datetime.datetime.strptime(data_str, "%m/%d/%Y").date()
print(formata_data(data))
print(data_futuro(data))
