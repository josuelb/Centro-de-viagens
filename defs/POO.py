from time import sleep
from js import function



def cadastrar():
    viagem = ''

    name = input('Seu nome completo: ')
    sleep(0.3)
    cpf = input('CPF: ')
    sleep(0.3)
    desc = str(input("Deseja marcar alguma viagem? [S/N] ").upper().strip())
    if desc == 'S':
        viagem = input('Para onde vamos? ')
    elif desc == 'N':
        print("Certo.")
    else:
        print("Resposta invalida. responda com 'S' para sim e 'N' para não.")
    sleep(0.5)

    dados = {'nome': name, 'cpf': cpf, 'viagem': viagem}

    function.adicionar(name, dados)


def look():
    name = input("Seu nome completo: ")
    function.ler(name)
