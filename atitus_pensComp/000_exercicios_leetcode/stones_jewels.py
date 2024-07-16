# https://leetcode.com/problems/jewels-and-stones/description/

joias = "z"
pedras = "ZZ"

conta_joias = 0
for letra in joias:
    total_de_joias = pedras.count(letra)
    conta_joias = conta_joias + total_de_joias

print(conta_joias)
