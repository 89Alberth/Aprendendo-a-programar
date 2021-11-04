num = int(input('Digite um número: '))
soma = 0
for c in range(1, num + 1):
    if num % c == 0:
        soma = soma + 1
        print('\033[0;32m', end='')
    else:
        print('\033[0;33m', end='')

    print(c, end=' ')
if soma == 2:
    print('\033[m \n O número {} é um número PRIMO'.format(num))
else:
    print('\033[m \nO número {} não é um número primo.'.format(num))