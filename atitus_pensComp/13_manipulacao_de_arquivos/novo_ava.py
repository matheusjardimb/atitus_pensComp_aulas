import os


def cria_pasta_curso(nome_curso: str) -> None:
    nome_curso = nome_curso.replace(" ", "_").lower()
    if not os.path.exists(nome_curso):
        os.mkdir(nome_curso)
        print(f"Pasta do curso '{nome_curso}' criada")


def cria_alunos(alunos: list, nome_curso: str) -> None:
    caminho_arquivo = f"{nome_curso}/alunos.txt"
    if not os.path.exists(caminho_arquivo):
        file = open(caminho_arquivo, "w")
    else:
        file = open(caminho_arquivo, "a")
        file.writelines("\n")

    for aluno in alunos:
        file.writelines(f"{aluno}\n")
    return


def converte_alunos_em_lista():
    return alunos_str.split(",")


nome_curso = input("Informe o nome do curso: ")
cria_pasta_curso(nome_curso)

alunos_str = input("Informe o nome dos alunos separados por vírgula: ")
alunos_lista = converte_alunos_em_lista()
cria_alunos(alunos_lista, nome_curso)
