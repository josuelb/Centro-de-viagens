from time import sleep
from js import password, function


def cadastrar(res):
    print('Voçe digitou {}'.format(res))

    pessoa = {}

    name = str(input("Nome Completo: ").strip())

    p = input("Olá {}, deseja fazer alguma viagem agora? [S/N] ".format(name)).strip()
    if p == 'S':
        viagem = str(input("Deseja ir para onde? ").strip())
    else:
        viagem = ' '
        print("OKAY!")
    sleep(0.5)

    pessoa[name] = {
        "nome": name,
        "cpf": input("Seu CPF: ").strip(),
        "viagem": viagem
    }
    sleep(0.5)

    function.adicionar(pessoa, name)

    sleep(0.5)

    print(pessoa)


def cadastro(res):
    print('Voçe digitou {}'.format(res))
    sleep(0.5)
    password.password()


def look():
    name = input("Seu nome completo: ")
    function.ver()
