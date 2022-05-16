from time import sleep
from js import password, function


def cadastrar(res):
    print('Voçe digitou {}'.format(res))

    pessoa = {}

    Nome = str(input("Nome Completo: ").strip()).capitalize()

    p = input("Olá {}, deseja fazer alguma viagem agora? [S/N] ".format(Nome)).strip()
    if p == 'S':
        viagem = str(input("Deseja ir para onde? ").strip())
    else:
        viagem = ' '
        print("OKAY!")
    sleep(0.5)

    pessoa[Nome] = {
        "nome": Nome,
        "cpf": input("Seu CPF: ").strip(),
        "viagem": viagem
    }
    sleep(0.5)

    function.adicionar(pessoa)

    sleep(0.5)

    print(pessoa)


def cadastro(res):
    print('Voçe digitou {}'.format(res))
    sleep(0.5)

    password.password()

