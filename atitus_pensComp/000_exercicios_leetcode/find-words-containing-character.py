# https://leetcode.com/problems/find-words-containing-character/

palavras = ["vida", "esperanca", "python", "leet", "code"]
x = "e"

# RETORNA A LISTA COM A POSICAO DAS PALAVRAS QUE CONTENHA 'x'

resposta = []
for i in range(len(palavras)):
    if x in palavras[i]:
        resposta.append(i)

print(resposta)
