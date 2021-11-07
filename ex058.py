from random import randint
cont = 1
computer = randint(1, 10)
print('Olá sou seu computador adivinha o número que eu pensei...')
print('Será que consegue adivinhar?')
jogador = int(input('Escolha um números de 1 á 10: '))

while jogador != computer:

    if jogador < computer:
        print('Mais...tente outra vez.')
        jogador = int(input('Qual é seu palpite: '))
    else:
        print('Menos...tente outra vez.')
        jogador = int(input('Qual é seu palpite: '))
    cont = cont + 1

print('Parabéns acertou!')
print('Você precisou de {} tentativas.'.format(cont))

