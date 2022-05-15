import json


def adicionar(pessoa):
    json_object = json.dumps(pessoa, indent=4)
    with open("js/dados.json", "a") as outfile:
        outfile.write(json_object)