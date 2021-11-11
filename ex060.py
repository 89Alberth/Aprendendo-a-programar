from math import factorial
n = int(input('Digite um número para calcular seu fatorial: '))
c = n
f = factorial(n)
print('Calculando {}! '.format(n), end=' ')
while c > 0:
    print(c, end=' ')
    if c > 1:
        print('X', end=' ')
    else:
        print('=', end=' ')
    c = c - 1
print('\33[1;32m', f)

