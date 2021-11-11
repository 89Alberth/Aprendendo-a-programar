print('-=' * 15)
print('sequência de fibonacci')
print('-=' * 15)
n = int(input('Digite quantos termos deseja análisa: '))
t1 = 0
t2 = 1
cont = 3
print('{} → {}'.format(t1, t2), end='')

while cont <= n:
    t3 = t1 + t2
    print(' → {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    cont += 1

print(' → FIM', end='')
