import json


def adicionar(pessoa, name):
    out_file = json.dumps(pessoa, indent=4)
    with open(f"js/json/{name}.json", 'w', newline='', encoding='utf-8') as outfile:
        outfile.write(out_file)


def ler(name):
    file = open(f"js/json/{name}.json")
    dados = file.read()
    print(dados)


def ver(name):
    file = open(f"js/json/{name}.json")
    dado = file.read()
    print(dado["viagem"])