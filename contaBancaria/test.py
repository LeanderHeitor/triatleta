import requests
print("verificando endereço")
cep = input("digite o cep: ")
if len(cep)!=8:
    print("cep invalido")
    exit()
consulta = requests.get(f"https://viacep.com.br/ws/{cep}/json/")
print(consulta.json())