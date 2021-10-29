a = int(input('Primeiro numero: '))
b = int(input('Segundo numero: '))
c = int(input('terceiro numero: '))
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
print('O menor valor é {}.'.format(menor))
maior = c
if b > a and b > c:
    maior = b
if a > c and a > b:
    maior = a
print('O maior numero é {}.'.format(maior))
