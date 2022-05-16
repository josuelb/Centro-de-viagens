from time import sleep
from defs import POO

i = True

while i == True:
    title = 'CENTRO DE TURISMO'
    print(title)

    op1 = """
        1-Cadastrar
        2-Ver cadastros
        3-ver viagem
        4-Sair
    """
    print(op1)

    res = int(input("O que deseja? ").strip())
    sleep(0.5)

    if type(res) != int:
        print("Digite um NÚMERO!!!!")


    if res == 1:
        POO.cadastrar(res)
    elif res == 2:
        POO.cadastro(res)
