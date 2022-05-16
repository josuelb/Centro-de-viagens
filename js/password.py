import json
from js import function


def password(name):
    p = 'arrebatamento2'
    while True:
        sen = input("Senha de Administrador: ")

        if sen == p:
            function.ler(name)
            break
        else:
            print('Errada. Tente novamente!!!')

    json_object = json.dumps(p, indent=True)
    with open("js/pass.json", "w", newline='', encoding='UTF-8') as outfile:
        outfile.write(json_object)