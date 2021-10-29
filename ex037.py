num = int(input('Digite um número: '))
print('''Escolha a base para conversão.
[1] Binário
[2] octal
[3] Hexadecimal''')
opçao = int(input('Sua opção: '))

if opçao == 1:
    print('{} convertido para BINÁRIO é {}.'.format(num, bin(num)[2:]))
elif opçao == 2:
    print('{} convertido para OCTAL é {}.'.format(num, oct(num)[2:]))
elif opçao == 3:
    print('{} convertido para HEXADECIMAL é {}.'.format(num, hex(num)[2:]))
else:
    print('opção inválida tente novamente.')