import json
from js import function


def password():
    p = 'arrebatamento2'
    while True:
        sen = input("Senha de Administrador: ")

        if sen == p:
            function.ler()
            break
        else:
            print('Errada. tente novamente')

    json_object = json.dumps(p, indent=True)
    with open("js/pass.json", "a", newline='', encoding='UTF-8') as outfile:
        outfile.write(json_object)