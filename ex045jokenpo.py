from random import randint
from time import sleep
import emoji

itens = ('Pedra', 'Papel', 'Tesoura')
computer = randint(0, 2)

print('''
[0] PEDRA
[1] PAPEL
[2]TESOURA''')

print('-=' * 11)

jogador = int(input('Escolha sua opçâo: '))
if jogador == 0 or jogador == 1 or jogador == 2:
    print('-=' * 11)
    print('PEDRA')
    sleep(1)
    print('PAPEL')
    sleep(1)
    print('TESOURA...')
    sleep(1)
    print('-=' * 11)

    if computer == 0:    #computador jogou pedra
        if jogador == 0:
            print('EMPATE')
        elif jogador == 1:
            print('jogador VENCEU')
        elif jogador == 2:
            print('Computador VENCEU')

    elif computer == 1:  #computador jogou papel
        if jogador == 0:
            print('Computador VENCEU')
        elif jogador == 1:
            print('EMPATE')
        elif jogador == 2:
            print('Jogador VENCEU')

    elif computer == 2:   #computador jogou tesoura
        if jogador == 0:
            print('Jogador VENCEU')
        elif jogador == 1:
            print('Jogador PERDEU')
        elif jogador  == 2:
            print('EMPATE')

    print('Computador jogou:{}'.format(itens[computer]))
    print('Jogador jogou:{}'.format(itens[jogador]))
else:
    print('''    \33[1;31m!!!OPÇÃO INVÁLIDA!!!
escolha [0]PEDRA,[1]PAPEL OU [2]TESOURA.''')


