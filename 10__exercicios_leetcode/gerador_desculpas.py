import random

INTRODUCOES = [
    # Matheus
    "Tudo bem? É o seguinte...",
    "Você não vai acreditar, mas",
    "Nem imagina o que vou te contar:",
    "Parece mentira mas",
    "Tentar eu tentei, porém",
    "Eu até queria, mas",
    # João V
    "Eu te juro que é verdade isso…",
    "Por ironia do destino…",
    # Augusto
    "Parece loucura, porém",
    "Isso soa estranho, mas",
    # Felipe
    "O meu computador é ruim",
    "Bah… nem te conto",
    "então…",
    "Faltou luz em casa",
    "Roubaram minha conta no mine",
    "Perdi o monitor do meu computador",
    # Lafayete
    "Bom dia! então…",
    "Deus sempre sabe o que é melhor pra gente, e tendo isso em vista…",
    # Lucas
    "eu pensei que estava sonhando, mas",
    # Kaua
    "Por incrível que pareça",
    "Acredite se quiser, mas",
]

OBJETOS = [
    # Matheus
    "a Steam",
    "o dungeon master",
    "o Mark Zuckerberg",
    "o cachorro do vizinho",
    "meu pokemon favorito",
    "o ET Bilú",
    "o Zé Gotinha",
    # Joao V
    " a barata da vizinha…",
    # Augusto
    "o kung Fu Panda",
    "o Mestre Splinter",
    # Lucas
    " o Curupira",
    # Rafael
    "O phyton",
    # Lafayete
    "meu gato",
    "o meu professor de pensamento computacional",
    # Lucas
    "o curupira",
    "O ChatGPT",
    # Kauã
    "A minha tia",
    " meu cachorro",
]
EVENTOS = [
    # Matheus
    "roubou minha bicicleta",
    "hackeou meu instagram",
    "nerfou meu mago lv 30",
    "me venceu com o Exódia",
    "não sabe tocar piano",
    "pôs meu nome no Death Note",
    # Augusto
    "está dando banho no meu peixe.",
    "mandou 50 pizzas para minha casa.",
    # Lucas
    "não fez a parte dele",
    "tava lendo one piece",
    # Rafael
    "Me envenenou",
    "Roubou o alfabeto",
    # Lafayete
    "pegou fogo",
    "tava dormindo em cima do computador",
]


def string_aleatoria(opcoes: list) -> str:
    return random.choice(opcoes)


def gerador_desculpas(tarefa: str) -> str:
    introducao = string_aleatoria(INTRODUCOES)
    objeto = string_aleatoria(OBJETOS)
    evento = string_aleatoria(EVENTOS)
    return f"{introducao} {tarefa} porque {objeto} {evento}"


def main():
    tarefa = input('Digite uma tarefa (como "não fiz o entregável"): ')
    print("Escolha uma das opções abaixo:")
    for i in range(10):
        desculpas = gerador_desculpas(tarefa)
        print(f"{i}. {desculpas}")


main()
