import os

pasta = "minha_pasta"
if not os.path.exists(pasta):
    os.mkdir(pasta)
    print(f"A pasta '{pasta}' foi criada com sucesso.")
else:
    print(f"A pasta '{pasta}' já existe.")


# import os
#
# def retorna_conteudo(nome_arquivo: str) -> str:
#     existe_arquivo = os.path.exists(nome_arquivo)
#     if existe_arquivo:
#         with open(nome_arquivo) as arquivo:
#             return arquivo.read()
#     return None
#
#
#
# print(retorna_conteudo('arquivo.txt'))
# print(retorna_conteudo('arquivo_fake.txt'))

#
# existe_pasta = os.path.exists('minha_pasta1/pasta2/pasta3/arquivo.txt')
# print('minha_pasta/arquivo.txt', existe_pasta)
#
#
#


# with open("arquivo.txt", "r") as arquivo:
#     print(arquivo.readline())
#     print(arquivo.readline())
#     print(arquivo.readline())
#
# arquivo = open("arquivo.txt", "r")
# print(arquivo.readline())
# print(arquivo.readline())
# print(arquivo.readline())
# arquivo.close()


# file = open("arquivo.txt", "r+")
#
# # print(file.readlines())
# # print(file.readline())
#
#
# # Escreve no arquivo
# file.write("First line\n")
# file.seek(5)
# file.write("Second line")
# file.writelines(["Third\n", 'Fourth\n' 'Fifth'])
#
# # Sempre feche um arquivo após usá-lo para liberar
# # recursos do sistema operacional
# file.close()
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# #
# # file = open("arquivo.txt", "r")
# #
# # content = file.read() # Lê todo o conteúdo do arquivo
# # print(content)
# #
# # # line = file.readline() # Lê uma linha do arquivo
# # # print(line)
# # #
# # # line = file.readline() # Lê uma linha do arquivo
# # # print(line)
# # #
# # # line = file.readline() # Lê uma linha do arquivo
# # # print(line)
# #
# # # lines = file.readlines() # Lê todas as linhas do arquivo em uma lista
# # # print('lines')
# # # print(lines)
# # # print(lines[1])
# # #
# # # print()
# # # print('join lines')
# # # print(''.join(lines))
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# # #### O arquivo já existir?
# # # r => não há erro, arquivo aberto e não alterado
# # # open('arquivo.txt', 'r')
# #
# #
# # # w => arquivo aberto e conteúdo apagado
# # # open('arquivo.txt', 'w')
# #
# # #### O arquivo não existir?
# # # r => há erro, falha a aplicação
# # # open('arquivo.txt', 'r')
# #
# # # w => arquivo vazio criado
# # # open('arquivo.txt', 'w')
# #
# # #### O arquivo já possuir conteúdo?
# # # r => não há erro, arquivo aberto e não alterado
# # # open('arquivo.txt', 'r')
# #
# # # w => arquivo aberto e conteúdo apagado
# # # open('arquivo.txt', 'w')
