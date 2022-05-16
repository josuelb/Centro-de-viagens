import json


def adicionar(pessoa, name):
    with open(f"js/json/{name}.json", 'w', newline='') as outfile:
        json.dump(pessoa, outfile, indent=True)


def ler(name):
    file = open(f"js/json/{name}.json")
    dados = json.load(file)
    print(dados)
    print(type(dados))


def ver(ver):
    file = open(f"js/json/{name}.json")
    dado = json.load(file)
    print(dado['viagem'])