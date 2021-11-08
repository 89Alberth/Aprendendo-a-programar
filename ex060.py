n = int(input('Digite um número para calcular seu fatorial: '))
c = n
f = 1
while c > 0:
    print(c, end=' ')
    if c > 1:
        print('X', end=' ')
    else:
        print('=', end=' ')
    f = c * f
    c = c - 1
print('\33[1;32m', f)

