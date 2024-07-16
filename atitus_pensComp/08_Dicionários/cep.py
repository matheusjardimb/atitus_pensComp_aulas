import http.client
import json

# Versão de código sem usar a biblioteca requests

cep = ""
ceps_conhecidos = []

LEN_CEP = 8

contador_consultas = 0
enderecos = {}
aux = "o"

while True:
    cep = input("Digite o seu cep:")
    if cep == "0":
        break

    if len(cep) != LEN_CEP:
        print("CEP inválido")
        continue

    is_valid = True
    for char in cep:
        if not char.isdigit():
            is_valid = False

    if not is_valid:
        print("CEP inválido")
        continue

    if cep in ceps_conhecidos:
        print("Já sabemos esta consulta")
        continue

    contador_consultas += 1

    url = f"/ws/{cep}/json/"
    conn = http.client.HTTPSConnection("viacep.com.br")
    conn.request("GET", url)
    response = json.loads(conn.getresponse().read().decode())
    conn.close()

    ceps_conhecidos.append(cep)

    uf = response["uf"]
    localidade = response["localidade"]

    if uf in enderecos:
        if localidade in enderecos[uf]:
            enderecos[uf][localidade].append(cep)
        else:
            enderecos[uf][localidade] = [
                cep,
            ]
    else:
        enderecos[uf] = {
            localidade: [
                cep,
            ]
        }

print("Você consultou um total de:", contador_consultas, "vezes")
print(enderecos)
