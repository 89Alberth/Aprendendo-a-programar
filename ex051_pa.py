print('     Termos de uma PA     ')
print('-=' * 15)
ter = int(input('Primeiro termo: '))
raz = int(input('Razão: '))
decimo = ter + (10-1) * raz
for c in range(ter, decimo + raz, raz ):
    print('{}'.format(c), end='→')
