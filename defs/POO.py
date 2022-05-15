from time import sleep
from js import function


def cadastrar(res):
    print('Voçe digitou {}'.format(res))

    pessoa = {}

    sleep(0.5)
    pessoa['nome'] = str(input("Nome Completo: ").strip())
    sleep(0.5)
    pessoa['CPF'] = input("Seu CPF: ").strip()
    sleep(0.5)
    p = input("Deseja fazer alguma viagem agora? [S/N] ").strip()
    if p == 'S':
        pessoa['viagem'] = str(input("Deseja ir para onde? ").strip())
    else:
        print("OKAY!")

    function.adicionar(pessoa)
    sleep(0.5)

    print(pessoa)


def cadastro(res):
    print('Voçe digitou {}'.format(res))
    sleep(0.5)

    name = str(input("Informe seu nome, por favor: "))
