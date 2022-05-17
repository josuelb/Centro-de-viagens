import json


def adicionar(nome, dados):
    with open(f"js/dados/{nome}.json", 'w', newline='\n') as outfile:
        json.dump(dados, outfile, indent=True)


def ler(name):
    file = open(f"js/dados/{name}.json")
    dados = json.load(file)
    print(dados)
