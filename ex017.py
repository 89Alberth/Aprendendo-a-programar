#forma matematica#
'''co = float(input('Qual o comprimento do cateto oposto: '))
ca = float(input('Qual  comprimento do cateto adjacente: '))
hi = (co ** 2 + ca ** 2) ** (1 / 2)
print('O valor da hipotenusa é {:.2f}.'.format(hi))'''

from math import hypot
co = float(input('Digite o cateto oposto: '))
ca = float(input('Digite o cateto adjacente: '))
hi = hypot(co, ca)
print('O valor da  hipotenusa é {}.'.format(hi))
