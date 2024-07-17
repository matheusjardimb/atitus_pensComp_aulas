import http.client
import json

cep = "91110000"
url = f"/ws/{cep}/json/"

conn = http.client.HTTPSConnection("viacep.com.br")
conn.request("GET", url)
response = json.loads(conn.getresponse().read().decode())
conn.close()

print(response)
print(response["logradouro"])
print(response["uf"])
