from random import randint
from time import sleep

computador = randint(0, 5)
print('-=-' * 20)
jogador = int(input('Escolha um número entre 0 a 5: '))
print('-=-' * 20 )
print('\033[1;0;33mProcessando...')
print('-=-' * 20)
sleep(4)

if jogador == computador:
    print('\033[1;32;40m!!!PARABÉNS VOCÊ VENCEU!!!\033[m \n O número sorteado foi {}'.format(computador))
else:
    print('\033[1;31;40m!!!VOCÊ PERDEU!!!\033[mÉ \n uma pena o número sorteado foi {} '.format(computador))
