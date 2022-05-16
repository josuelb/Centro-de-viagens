import json


def adicionar(pessoa):
    json_object = json.dumps(pessoa, indent=True)
    with open("js/dados.json", "a", newline='', encoding='UTF-8') as outfile:
        outfile.write('{},\n'.format(json_object))


def ler():
    dados = open("js/dados.json", "r")
    print(dados.read())
